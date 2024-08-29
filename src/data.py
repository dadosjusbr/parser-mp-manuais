import sys
import os
import subprocess
import pandas as pd
import glob

# Se for erro de não existir planilhas o retorno vai ser esse:
STATUS_DATA_UNAVAILABLE = 4
# Caso o erro for a planilha, que é invalida por algum motivo, o retorno vai ser esse:
STATUS_INVALID_FILE = 5


def _readXLS(file):
    try:
        dt = pd.read_excel(file, engine="xlrd")
        data = dt.to_numpy()
    except Exception as excep:
        print(f"Erro lendo as planilhas XLS ({file}): {excep}", file=sys.stderr)
        sys.exit(STATUS_INVALID_FILE)
    return data


def _readXLSX(file):
    try:
        dt = pd.read_excel(file, engine="openpyxl")
        data = dt.to_numpy()
    except Exception as excep:
        print(f"Erro lendo as planilhas XLS ({file}): {excep}", file=sys.stderr)
        sys.exit(STATUS_INVALID_FILE)
    return data


def _readODS(file):
    try:
        dt = pd.read_excel(file, engine="odf")
        data = dt.to_numpy()
    except Exception as excep:
        print(f"Erro lendo as planilhas ODS ({file}): {excep}", file=sys.stderr)
        sys.exit(STATUS_INVALID_FILE)
    return data


def _readCSV(file):
    try:
        dt = pd.read_csv(file, encoding="iso-8859-1", skiprows=1, delimiter=";")
        data = dt.to_numpy()
    except Exception as excep:
        print(f"Erro lendo as planilhas CSV ({file}): {excep}", file=sys.stderr)
        sys.exit(STATUS_INVALID_FILE)
    return data


def load(file_names, data):
    """Carrega os arquivos passados como parâmetros.
     :param file_names: slice contendo os arquivos baixados pelo coletor.
    Os nomes dos arquivos devem seguir uma convenção e começar com
    Membros ativos-contracheque e Membros ativos-Verbas Indenizatorias
     :param year e month: usados para fazer a validação na planilha de controle de dados
     :return um objeto Data() pronto para operar com os arquivos
    """

    if data.court.casefold() in ["mppa", "mpsc", "mprr"]:
        data.contracheque = _readXLS([c for c in file_names if "contracheque" in c][0])
        data.indenizatorias = _readXLS(
            [i for i in file_names if "indenizacoes" in i][0]
        )

        return data

    elif data.court.casefold() in [
        "mpsp",
        "mprj",
        "mpse",
        "mprn",
        "mpto",
        "mppi",
        "mpac",
        "mpba",
    ] or (data.court.casefold() == "mpes" and int(year) != 2021):
        data.contracheque = _readODS([c for c in file_names if "contracheque" in c][0])
        data.indenizatorias = _readODS(
            [i for i in file_names if "indenizacoes" in i][0]
        )

        return data

    elif data.court.casefold() in ["mprs", "mpal"]:
        data.contracheque = _readCSV([c for c in file_names if "contracheque" in c][0])
        data.indenizatorias = _readCSV(
            [i for i in file_names if "indenizacoes" in i][0]
        )

        return data

    elif data.court.casefold() in ["mppe"] or (
        data.court.casefold() == "mpes" and int(year) == 2021
    ):
        data.contracheque = _readXLSX([c for c in file_names if "contracheque" in c][0])
        data.indenizatorias = _readXLSX(
            [i for i in file_names if "indenizacoes" in i][0]
        )

        return data


class Data:
    def __init__(
        self, year, month, court, output_folder, contracheque=None, indenizatorias=None
    ):
        self.year = year
        self.month = month
        self.court = court
        self.output_folder = output_folder
        self.contracheque = contracheque
        self.indenizatorias = indenizatorias

    def validate(self):
        """
         Validação inicial dos arquivos passados como parâmetros.
        Aborta a execução do script em caso de erro.
         Caso o validade fique pare o script na leitura da planilha
        de controle de dados dara um erro retornando o codigo de erro 4,
        esse codigo significa que não existe dados para a data pedida.
        """

        if not (
            glob.glob(
                f"{self.output_folder}/{self.court}-contracheques-{self.month}-{self.year}.*"
            )
            and glob.glob(
                f"{self.output_folder}/{self.court}-indenizacoes-{self.month}-{self.year}.*"
            )
        ):
            sys.stderr.write(
                f"Não existe planilhas para {self.court}/{self.month}/{self.year}."
            )
            sys.exit(STATUS_DATA_UNAVAILABLE)
