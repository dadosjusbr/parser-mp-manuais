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
        # é necessário pular 1 linha no MPAL, pois o pandas entende a primeira linha 
        # (que contém apenas a data) como cabeçalho, deixando o dataframe quebrado, excluindo demais colunas 
        # e perdendo informações relevantes.
        # não é necessário fazer isso com o MPRS, pois a primeira linha é, de fato, o cabeçalho.
        if "mpal" in file.casefold():
            skiprows = 1
        else:
            skiprows = 0

        dt = pd.read_csv(file, encoding="iso-8859-1", skiprows=skiprows, delimiter=";")
        data = dt.to_numpy()
    except Exception as excep:
        print(f"Erro lendo as planilhas CSV ({file}): {excep}", file=sys.stderr)
        sys.exit(STATUS_INVALID_FILE)
    return data


def _convert_file(file):
    """
    Converte os arquivos ODT que estão corrompidos.
    """
    subprocess.run(
        ["libreoffice", "--headless", "--invisible", "--convert-to", "docx", file],
        capture_output=True,
        text=True,
    )  # Pega a saída para não interferir no print dos dados
    file_name = file.split(sep="/")[-1]
    file_name = f'{file_name.split(sep=".")[0]}'

    subprocess.run(
        [
            "libreoffice",
            "--headless",
            "--invisible",
            "--convert-to",
            "odt",
            f"{file_name}.docx",
        ],
        capture_output=True,
        text=True,
    )  # Pega a saída para não interferir no print dos dados

    file_name = f"{file_name}.odt"

    # Move para o diretório passado por parâmetro
    subprocess.run(["mv", file_name, f"{file}"])
    return f"{file}"


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
    ] or (data.court.casefold() == "mpes" and int(data.year) != 2021):
        if data.court.casefold() == "mpse":
            data.contracheque = _readODS(_convert_file([c for c in file_names if "contracheque" in c][0]))
        else:
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
        data.court.casefold() == "mpes" and int(data.year) == 2021
    ):
        if data.court.casefold() == "mppe" and int(data.year) == 2023 and int(data.month) not in [5,6,8]:
            data.contracheque = _readXLS([c for c in file_names if "contracheque" in c][0])
        else:
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
                f"{self.output_folder}/{self.court.upper()}-contracheques-{self.month}-{self.year}.*"
            )
            and glob.glob(
                f"{self.output_folder}/{self.court.upper()}-indenizacoes-{self.month}-{self.year}.*"
            )
        ):
            sys.stderr.write(
                f"Não existe planilhas para {self.court}/{self.month}/{self.year}."
            )
            sys.exit(STATUS_DATA_UNAVAILABLE)
