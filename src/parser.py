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
                # MPPI não informa cargo e lotação para todos os membros,
                # podendo colocar 2 campos nulos ou substituir algum por " ".
                # Isso dificulta ao iterar sobre as rubricas, uma vez que não há um padrão e não é estritamente tabular.
                if court == "mppi" and len(new_row) != 18:
                    new_row = ["" if item == " " else item for item in new_row]
                    while len(new_row) != 18:
                        new_row.insert(2, "")

                # Os dados do MPSE inclui também dados de servidores e membros inativos,
                # então filtramos para pegar apenas os dados de membros ativos
                if (
                    court == "mpse"
                    and new_row[2]
                    not in [
                        "PROMOTOR DE JUSTIÇA DE ENTR. FINAL",
                        "PROMOTOR DE JUSTIÇA DE ENTR. INICIAL",
                        "PROCURADOR DE JUSTIÇA",
                        "PROMOTOR DE JUSTIÇA SUBSTITUTO",
                    ]
                ) or (court == "mpse" and new_row[3] == "INATIVOS"):
                    continue
                # MPPA possui uma linha com o somatório de cada rubrica
                elif (
                    (court == "mppa" and len(new_row) == 15)
                    or (court == "mppe" and "página" in registration.casefold())
                    or (court == "mpes" and len(new_row) == 14)
                ):
                    continue
                # MPRN não possui lotação
                elif court == "mprn":
                    new_row = row
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


def remunerations_mpes(file_indenizatorias):
    dict_remuneracoes = {}
    for row in file_indenizatorias:
        if not pd.isna(row[0]):
            mat = str(row[0])
            remuneracoes = dict_remuneracoes.get(mat, Coleta.Remuneracoes())
            rem = Coleta.Remuneracao()
            rem.natureza = Coleta.Remuneracao.Natureza.Value("R")
            rem.categoria = "VERBAS INDENIZATÓRIAS"
            rem.item = str(row[4])
            rem.valor = float(number.format_value(row[5]))
            rem.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("O")
            remuneracoes.remuneracao.append(rem)
            if not pd.isna(row[6]):
                rem = Coleta.Remuneracao()
                rem.natureza = Coleta.Remuneracao.Natureza.Value("R")
                rem.categoria = "OUTRAS REMUNERAÇÕES TEMPORÁRIAS"
                rem.item = str(row[6])
                rem.valor = float(number.format_value(row[7]))
                rem.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("O")
                remuneracoes.remuneracao.append(rem)
            dict_remuneracoes[mat] = remuneracoes
    return dict_remuneracoes


def remunerations_mppa(row, header):
    remuneration_array = Coleta.Remuneracoes()
    # VERBAS INDENIZATÓRIAS
    for key, value in header.items():
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


def get_remunerations_mpes(employee, remuneracoes):
    if employee in remuneracoes.keys():
        return remuneracoes[employee]


def update_employees(file_indenizacoes, employees, court):
    for row in file_indenizacoes:
        if court in ["mpto", "mppi", "mpse"]:
            row = [x for x in row if not pd.isna(x)]
        if len(row) > 1:
            if court in ["mprn", "mpal", "mprr"]:
                registration = row[1]
            else:
                registration = row[0]

            if (
                type(registration) != str
                and not pd.isna(registration)
                and court == "mprj"
            ):
                registration = str(int(registration)).zfill(8)

            if type(registration) != str and not pd.isna(registration):
                registration = str(int(registration))

            if registration in employees.keys():
                emp = employees[registration]
                remu = remunerations(row, court)
                emp.remuneracoes.MergeFrom(remu)
                employees[registration] = emp
    return employees


def get_mppe_header(year, month):
    if year == 2021 and month < 12:
        return "mppe-01-2021"
    elif (year == 2021 and month == 12) or (year == 2022 and month < 12):
        return "mppe-12-2021"
    elif year == 2022 and month == 12:
        return "mppe-12-2022"
    else:
        return "mppe-01-2023"


def update_employees_mppe(data, employees):
    header = get_mppe_header(int(data.year), int(data.month))

    for row in data.indenizatorias:
        registration = row[0]

        if type(registration) != str and not pd.isna(registration):
            registration = str(int(registration))

        if registration in employees.keys():
            emp = employees[registration]
            remu = remunerations(row, header)
            emp.remuneracoes.MergeFrom(remu)
            employees[registration] = emp

    return employees


def get_mpac_header(year, month):
    if year == 2021:
        if month == 1:
            return "mpac-01-2021"
        elif month == 2:
            return "mpac-02-2021"
        elif month == 3:
            return "mpac-03-2021"
        elif month == 4:
            return "mpac-04-2021"
        elif month == 5:
            return "mpac-05-2021"
        elif month == 6:
            return "mpac-06-2021"
        elif month >= 7:
            return "mpac-07-2021"
    elif year == 2022 and month in [1, 2]:
        return "mpac-01-2022"
    elif year == 2022 and month == 11:
        return "mpac-11-2022"
    elif year == 2023 and month == 7:
        return "mpac-07-2023"
    elif (year == 2022 and month >= 3) or (year == 2023 and month <= 8):
        return "mpac-03-2022"
    elif year == 2023 and month in [9, 10, 11]:
        return "mpac-09-2023"
    else:
        return "mpac-12-2023"


def update_employees_mpac(data, employees):
    header = get_mpac_header(int(data.year), int(data.month))

    for row in data.indenizatorias:
        if int(data.year) != 2021 or (int(data.year) == 2021 and int(data.month) >= 7):
            row = [x for x in row if not pd.isna(x)]

        if len(row) != 0:
            registration = row[0]

            if type(registration) != str and not pd.isna(registration):
                registration = str(int(registration))

            if registration in employees.keys():
                emp = employees[registration]
                remu = remunerations(row, header)
                emp.remuneracoes.MergeFrom(remu)
                employees[registration] = emp

    return employees


def get_mpes_header(year, month):
    if month in [1, 3]:
        return "mpes-01-2021"
    elif month in [2, 7]:
        return "mpes-02-2021"
    elif month in [8]:
        return "mpes-08-2021"
    elif month in [12]:
        return "mpes-12-2021"
    else:
        # month in [4,5,6,9,10,11]
        return "mpes-04-2021"


def update_employees_mpes(data, employees):
    # Os diversos formatos do MPES em 2021 possui suas rubricas em colunas,
    # isto é, precisamos listar suas rubricas e interamos apenas pelos seus valores,
    # assim como os demais órgãos.
    # A partir de 2022, temos 2 colunas (ou 4), uma contendo a descrição/rubrica e outra contendo o valor.
    if int(data.year) == 2021:
        header = get_mpes_header(2021, int(data.month))

        for row in data.indenizatorias:
            registration = row[0]

            if type(registration) != str and not pd.isna(registration):
                registration = str(int(registration))

            if registration in employees.keys():
                emp = employees[registration]
                remu = remunerations(row, header)
                emp.remuneracoes.MergeFrom(remu)
                employees[registration] = emp
    else:
        remuneracoes = remunerations_mpes(data.indenizatorias)
        for employee in employees:
            emp = employees[employee]
            remu = get_remunerations_mpes(employee, remuneracoes)
            emp.remuneracoes.MergeFrom(remu)
            employees[employee] = emp
    return employees


def get_mprj_header(year, month):
    header = "mprj"

    if year == 2022 and month in [10]:
        header = "mprj-10-2022"
    elif year == 2023:
        if month in [5, 6, 9, 10]:
            header = "mprj-05-2023"
        elif month in [7, 8]:
            header = "mprj-07-2023"

    return header


def update_employees_mprj(data, employees):
    # Mudança de formato de planilha do MPES em alguns meses
    # em 2022 e 2023
    header = get_mprj_header(int(data.year), int(data.month))

    for row in data.indenizatorias:
        registration = row[0]

        if type(registration) != str and not pd.isna(registration):
            registration = str(int(registration)).zfill(8)

        if registration in employees.keys():
            emp = employees[registration]
            remu = remunerations(row, header)
            emp.remuneracoes.MergeFrom(remu)
            employees[registration] = emp

    return employees


def get_mpsp_header(year, month):
    header = "mpsp"

    if year in [2021, 2022]:
        if year == 2022 and month == 2:
            header = "mpsp-02-2022"
        elif (year == 2022 and month in [3, 4, 5, 6, 7]) or (
            year == 2021 and month in [6, 7, 8, 9, 12]
        ):
            header = "mpsp-03-2022"
        elif month in [8, 9, 10, 11, 12]:
            header = "mpsp-08-2022"
    elif year == 2023:
        if month == 1:
            header = "mpsp-01-2023"
        elif month in [2, 3, 4, 5, 6]:
            header = "mpsp-08-2022"
        elif month in [7, 8, 9, 10, 11, 12]:
            header = "mpsp-03-2022"

    return header


def update_employees_mpsp(data, employees):
    header = get_mpsp_header(int(data.year), int(data.month))

    for row in data.indenizatorias:
        registration = row[0]

        if type(registration) != str and not pd.isna(registration):
            registration = str(int(registration))

        if registration in employees.keys():
            emp = employees[registration]
            remu = remunerations(row, header)
            emp.remuneracoes.MergeFrom(remu)
            employees[registration] = emp

    return employees


def get_mpse_header(year, month):
    if year == 2021 and month == 1:
        return "mpse-01-2021"
    elif (year == 2021 and month > 1) or (year == 2022 and month < 3):
        return "mpse-02-2021"
    elif year == 2022 and month in [3, 4, 5, 6, 7]:
        return "mpse-03-2022"
    elif year == 2022 and month in [8, 9]:
        return "mpse-08-2022"
    elif (year == 2022 and month > 9) or (year == 2023 and month < 8):
        return "mpse-10-2022"
    elif year == 2023 and month in [8, 9]:
        return "mpse-08-2023"
    else:
        return "mpse-10-2023"


def update_employees_mpse(data, employees):
    # MPSE mudou sua estrutura (rubricas) diversas vezes entre 2021 e 2023
    header = get_mpse_header(int(data.year), int(data.month))

    for row in data.indenizatorias:
        row = [x for x in row if not pd.isna(x)]
        registration = row[0]

        if type(registration) != str and not pd.isna(registration):
            registration = str(int(registration))

        if registration in employees.keys():
            emp = employees[registration]
            remu = remunerations(row, header)
            emp.remuneracoes.MergeFrom(remu)
            employees[registration] = emp

    return employees


def get_mpto_header(year, month):
    if year == 2021 and month < 8:
        return "mpto-01-2021"
    elif (year == 2021 and month >= 8) or (year == 2022 and month < 3):
        return "mpto-08-2021"
    elif year == 2022 and month in [3, 4, 5, 6]:
        return "mpto-03-2022"
    else:
        return "mpto-07-2022"


def update_employees_mpto(data, employees):
    header = get_mpto_header(int(data.year), int(data.month))

    for row in data.indenizatorias:
        row = [x for x in row if not pd.isna(x)]
        if len(row) > 0:
            registration = row[0]

            if type(registration) != str and not pd.isna(registration):
                registration = str(int(registration))

            if registration in employees.keys():
                emp = employees[registration]
                remu = remunerations(row, header)
                emp.remuneracoes.MergeFrom(remu)
                employees[registration] = emp

    return employees


def update_employees_mppa(data, employees):
    # O cabeçalho da planilha de indenizações do MPPA muda todo mês
    # No entanto, ainda segue um padrão mínimo, o que nos permite iterar sobre as rubricas.
    columns = data.indenizatorias[0][7:]
    header = {}
    count = 7

    for col in columns:
        if "Subtotal" not in col:
            header[col] = count
        count += 1

    for row in data.indenizatorias:
        registration = row[0]
        if type(registration) != str and not pd.isna(registration):
            registration = str(int(registration))

        if registration in employees.keys():
            emp = employees[registration]
            remu = remunerations_mppa(row, header)
            emp.remuneracoes.MergeFrom(remu)
            employees[registration] = emp

    return employees


def parse(data, colect_key):
    employees = {}
    payroll = Coleta.FolhaDePagamento()

    employees.update(
        parse_employees(data.contracheque, colect_key, data.court.casefold())
    )

    # Alguns órgãos mudaram o formato de sua planilha de indenizações diversas vezes entre 2021 e 2023
    if data.court.casefold() == "mpes":
        update_employees_mpes(data, employees)
    elif data.court.casefold() == "mpse":
        update_employees_mpse(data, employees)
    elif data.court.casefold() == "mppe":
        update_employees_mppe(data, employees)
    elif data.court.casefold() == "mprj":
        update_employees_mprj(data, employees)
    elif data.court.casefold() == "mpsp":
        update_employees_mpsp(data, employees)
    elif data.court.casefold() == "mpto":
        update_employees_mpto(data, employees)
    elif data.court.casefold() == "mpac":
        update_employees_mpac(data, employees)
    elif data.court.casefold() == "mppa":
        update_employees_mppa(data, employees)
    else:
        update_employees(data.indenizatorias, employees, data.court.casefold())

    for i in employees.values():
        payroll.contra_cheque.append(i)

    return payroll
