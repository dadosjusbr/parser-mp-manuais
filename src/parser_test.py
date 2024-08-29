from parser import parse
import unittest
import json
from google.protobuf.json_format import MessageToDict
import data


class TestParser(unittest.TestCase):
    # Nem todos os membros do MPPI possuem cargo e lotação, 
    # verificamos se a listagem dos dados dos membros e rubricas estão corretas
    def test_mppi_09_2022(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mppi_09_2022.json", "r") as fp:
            expected_09_2022 = json.load(fp)

        files = [
            "src/output_test/sheets/MPPI-contracheques-09-2022.ods",
            "src/output_test/sheets/MPPI-indenizacoes-09-2022.ods",
        ]

        dados = data.Data("2022", "09", "MPPI", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mppi/09/2022")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_09_2022, result_to_dict["contraCheque"][2:4])
