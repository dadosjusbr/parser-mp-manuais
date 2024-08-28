import sys
import os

import number
import pandas as pd

from coleta import coleta_pb2 as Coleta

from headers_keys import *


def parse_employees(file, colect_key, court):
    employees = {}
    counter = 1

    for row in file:
        # Isso é necessário pois alguns órgãos não são estritamente tabulares
        new_row = [x for x in row if not pd.isna(x)]

        if len(new_row) > 1:
            # Precisamos disso pois o pandas entende que a matrícula é um número float.
            registration = str(new_row[0])

            if (
                "fonte da informação" in registration.casefold()
                or "total geral" in registration.casefold()
            ):
                break

            # Restrições referente aos cabeçalhos das planilhas
            if (
                registration.casefold()
                not in [
                    "matrícula",
                    "matricula",
                    "total geral",
                    "nome",
                    "matrã\xadcula",
                ]
                and "remunera" not in registration.casefold()
                and "competência" not in registration.casefold()
                and "cargo efetivo" not in registration.casefold()
                and "grupo" not in registration.casefold()
                and "rendimento" not in registration.casefold()
                and "mês" not in registration.casefold()
            ):
                # MPPA possui uma linha com o somatório de cada rubrica
                if (
                    (court == "mppa" and len(new_row) == 15)
                    or (court == "mppe" and "página" in registration.casefold())
                    or (court == "mpes" and len(new_row) == 14)
                ):
                    continue
                # MPRN não possui lotação
                elif court == "mprn":
                    registration = str(new_row[1])
                    name = new_row[0]
                    funcao = new_row[2]
                    local_trabalho = ""
                # MPAL não possui matrícula
                elif court == "mpal":
                    registration = ""
                    name = new_row[0]
                    funcao = new_row[1]
                    local_trabalho = new_row[2]
                else:
                    name = new_row[1]
                    funcao = new_row[2]
                    local_trabalho = new_row[3]

                member = Coleta.ContraCheque()
                member.id_contra_cheque = colect_key + "/" + str(counter)
                member.chave_coleta = colect_key
                member.matricula = registration
                member.nome = name
                member.funcao = funcao
                member.local_trabalho = local_trabalho
                member.tipo = Coleta.ContraCheque.Tipo.Value("MEMBRO")
                member.ativo = True

                member.remuneracoes.CopyFrom(create_remuneration(new_row, court))

                employees[str(new_row[0])] = member
                counter += 1

    return employees


def create_remuneration(row, court):
    remuneration_array = Coleta.Remuneracoes()
    headers_contracheque = f"contracheque-{court}"
    # REMUNERAÇÃO BÁSICA
    for key, value in HEADERS[headers_contracheque]["REMUNERAÇÃO BÁSICA"].items():
        remuneration = Coleta.Remuneracao()
        remuneration.natureza = Coleta.Remuneracao.Natureza.Value("R")
        remuneration.categoria = "REMUNERAÇÃO BÁSICA"
        remuneration.item = key
        remuneration.valor = float(number.format_value(row[value]))
        remuneration.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("B")
        remuneration_array.remuneracao.append(remuneration)
    # REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA
    for key, value in HEADERS[headers_contracheque][
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA"
    ].items():
        remuneration = Coleta.Remuneracao()
        remuneration.natureza = Coleta.Remuneracao.Natureza.Value("R")
        remuneration.categoria = "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA"
        remuneration.item = key
        remuneration.valor = float(number.format_value(row[value]))
        remuneration.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("B")
        remuneration_array.remuneracao.append(remuneration)
    # OBRIGATÓRIOS/LEGAIS
    for key, value in HEADERS[headers_contracheque]["OBRIGATÓRIOS/LEGAIS"].items():
        remuneration = Coleta.Remuneracao()
        remuneration.natureza = Coleta.Remuneracao.Natureza.Value("D")
        remuneration.categoria = "OBRIGATÓRIOS/LEGAIS"
        remuneration.item = key
        remuneration.valor = abs(float(number.format_value(row[value]))) * (-1)
        remuneration_array.remuneracao.append(remuneration)

    return remuneration_array


def remunerations(row, court):
    remuneration_array = Coleta.Remuneracoes()
    headers_indenizacoes = f"indenizacoes-{court}"
    # VERBAS INDENIZATÓRIAS
    for key, value in HEADERS[headers_indenizacoes].items():
        remuneration = Coleta.Remuneracao()
        remuneration.natureza = Coleta.Remuneracao.Natureza.Value("R")
        remuneration.categoria = (
            "VERBAS INDENIZATÓRIAS E OUTRAS REMUNERAÇÕES TEMPORÁRIAS"
        )
        remuneration.item = key
        remuneration.valor = float(number.format_value(row[value]))
        remuneration.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("O")
        remuneration_array.remuneracao.append(remuneration)
    return remuneration_array


def update_employees(file_indenizacoes, employees, court):
    for row in file_indenizacoes:
        if court in ["mpto", "mppi", "mpse"]:
            row = [x for x in row if not pd.isna(x)]
        if len(row) > 1:
            if court in ["mprn", "mpal", "mprr"]:
                registration = row[1]
            else:
                registration = row[0]

            if type(registration) != str and not pd.isna(registration):
                registration = str(int(registration))

            if registration in employees.keys():
                emp = employees[registration]
                remu = remunerations(row, court)
                emp.remuneracoes.MergeFrom(remu)
                employees[registration] = emp
    return employees


def parse(data, colect_key):
    employees = {}
    payroll = Coleta.FolhaDePagamento()

    employees.update(
        parse_employees(data.contracheque, colect_key, data.court.casefold())
    )
    update_employees(data.indenizatorias, employees, data.court.casefold())

    for i in employees.values():
        payroll.contra_cheque.append(i)

    return payroll