import sys
import data
import os
from parser import parse
from coleta import coleta_pb2 as Coleta, IDColeta
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf import text_format

if "COURT" in os.environ:
    court = os.environ["COURT"]
else:
    sys.stderr.write("Invalid arguments, missing parameter: 'COURT'.\n")
    os._exit(1)

if "YEAR" in os.environ:
    year = os.environ["YEAR"]
else:
    sys.stderr.write("Invalid arguments, missing parameter: 'YEAR'.\n")
    os._exit(1)

if "MONTH" in os.environ:
    month = os.environ["MONTH"]
    month = month.zfill(2)
else:
    sys.stderr.write("Invalid arguments, missing parameter: 'MONTH'.\n")
    os._exit(1)

if "PARSER_VERSION" in os.environ:
    PARSER_VERSION = os.environ["PARSER_VERSION"]
else:
    PARSER_VERSION = "unspecified"

if "OUTPUT_FOLDER" in os.environ:
    output_path = os.environ["OUTPUT_FOLDER"]
else:
    output_path = "/output"


def parse_execution(data, file_names):
    # Cria objeto com dados da coleta.
    coleta = Coleta.Coleta()
    coleta.chave_coleta = IDColeta(court.casefold(), month, year)
    coleta.orgao = court.casefold()
    coleta.mes = int(month)
    coleta.ano = int(year)
    coleta.repositorio_parser = "https://github.com/dadosjusbr/parser-mp"
    coleta.versao_parser = PARSER_VERSION
    coleta.arquivos.extend(file_names)
    timestamp = Timestamp()
    timestamp.GetCurrentTime()
    coleta.timestamp_coleta.CopyFrom(timestamp)

    # Consolida folha de pagamento
    payroll = Coleta.FolhaDePagamento()
    payroll = parse(data, coleta.chave_coleta)

    # Monta resultado da coleta.
    rc = Coleta.ResultadoColeta()
    rc.folha.CopyFrom(payroll)
    rc.coleta.CopyFrom(coleta)

    # Imprime a versão textual na saída padrão.
    print(text_format.MessageToString(rc), flush=True, end="")


def main():
    file_names = [f.rstrip() for f in sys.stdin.readlines()]

    dados = data.Data(year, month, court, output_path)

    dados.validate()

    dados = data.load(file_names, dados)

    parse_execution(dados, file_names)


if __name__ == "__main__":
    main()
