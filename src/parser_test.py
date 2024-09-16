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

    # MPES muda o formato de sua planilha de indenizações diversas vezes entre 2021 e 2022
    def test_mpes_01_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpes_01_2021.json", "r") as fp:
            expected_01_2021 = json.load(fp)

        files = [
            "src/output_test/sheets/MPES-contracheques-01-2021.xlsx",
            "src/output_test/sheets/MPES-indenizacoes-01-2021.xlsx",
        ]

        dados = data.Data("2021", "01", "MPES", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpes/01/2021")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_01_2021, result_to_dict["contraCheque"][0])

    def test_mpes_02_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpes_02_2021.json", "r") as fp:
            expected_02_2021 = json.load(fp)

        files = [
            "src/output_test/sheets/MPES-contracheques-02-2021.xlsx",
            "src/output_test/sheets/MPES-indenizacoes-02-2021.xlsx",
        ]

        dados = data.Data("2021", "02", "MPES", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpes/02/2021")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_02_2021, result_to_dict["contraCheque"][0])

    def test_mpes_04_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpes_04_2021.json", "r") as fp:
            expected_04_2021 = json.load(fp)

        files = [
            "src/output_test/sheets/MPES-contracheques-04-2021.xlsx",
            "src/output_test/sheets/MPES-indenizacoes-04-2021.xlsx",
        ]

        dados = data.Data("2021", "04", "MPES", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpes/04/2021")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_04_2021, result_to_dict["contraCheque"][0])

    def test_mpes_08_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpes_08_2021.json", "r") as fp:
            expected_08_2021 = json.load(fp)

        files = [
            "src/output_test/sheets/MPES-contracheques-08-2021.xlsx",
            "src/output_test/sheets/MPES-indenizacoes-08-2021.xlsx",
        ]

        dados = data.Data("2021", "08", "MPES", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpes/08/2021")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_08_2021, result_to_dict["contraCheque"][0])

    def test_mpes_12_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpes_12_2021.json", "r") as fp:
            expected_12_2021 = json.load(fp)

        files = [
            "src/output_test/sheets/MPES-contracheques-12-2021.xlsx",
            "src/output_test/sheets/MPES-indenizacoes-12-2021.xlsx",
        ]

        dados = data.Data("2021", "12", "MPES", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpes/12/2022")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_12_2021, result_to_dict["contraCheque"][0])

    def test_mpes_01_2022(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpes_01_2022.json", "r") as fp:
            expected_01_2022 = json.load(fp)

        files = [
            "src/output_test/sheets/MPES-contracheques-01-2022.ods",
            "src/output_test/sheets/MPES-indenizacoes-01-2022.ods",
        ]

        dados = data.Data("2022", "01", "MPES", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpes/01/2022")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_01_2022, result_to_dict["contraCheque"][0])


    # Problemas com colunas nulas resultava em rubricas com valores incorretos
    def test_mprn_01_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mprn_01_2021.json", "r") as fp:
            expected_01_2021 = json.load(fp)

        files = [
            "src/output_test/sheets/MPRN-contracheques-01-2021.ods",
            "src/output_test/sheets/MPRN-indenizacoes-01-2021.ods",
        ]

        dados = data.Data("2021", "01", "MPRN", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mprn/01/2021")
        
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_01_2021, result_to_dict["contraCheque"][0])


    def test_mppe_01_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mppe_01_2021.json", "r") as fp:
            expected_01_2021 = json.load(fp)

        files = [
            "src/output_test/sheets/MPPE-contracheques-01-2021.xlsx",
            "src/output_test/sheets/MPPE-indenizacoes-01-2021.xlsx",
        ]

        dados = data.Data("2021", "01", "MPPE", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mppe/01/2021")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_01_2021, result_to_dict["contraCheque"][0])


    def test_mppe_12_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mppe_12_2021.json", "r") as fp:
            expected_12_2021 = json.load(fp)

        files = [
            "src/output_test/sheets/MPPE-contracheques-12-2021.xlsx",
            "src/output_test/sheets/MPPE-indenizacoes-12-2021.xlsx",
        ]

        dados = data.Data("2021", "12", "MPPE", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mppe/12/2021")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_12_2021, result_to_dict["contraCheque"][0])

    def test_mppe_12_2022(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mppe_12_2022.json", "r") as fp:
            expected_12_2022 = json.load(fp)

        files = [
            "src/output_test/sheets/MPPE-contracheques-12-2022.xlsx",
            "src/output_test/sheets/MPPE-indenizacoes-12-2022.xlsx",
        ]

        dados = data.Data("2022", "12", "MPPE", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mppe/12/2022")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_12_2022, result_to_dict["contraCheque"][0])

    def test_mppe_01_2023(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mppe_01_2023.json", "r") as fp:
            expected_01_2023 = json.load(fp)

        files = [
            "src/output_test/sheets/MPPE-contracheques-01-2023.xls",
            "src/output_test/sheets/MPPE-indenizacoes-01-2023.xlsx",
        ]

        dados = data.Data("2023", "01", "MPPE", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mppe/01/2023")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_01_2023, result_to_dict["contraCheque"][0])
    
    def test_mpsp_01_2022(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpsp_01_2022.json", "r") as fp:
            expected_01_2022 = json.load(fp)

        files = [
            "src/output_test/sheets/MPSP-contracheques-01-2022.ods",
            "src/output_test/sheets/MPSP-indenizacoes-01-2022.ods",
        ]

        dados = data.Data("2022", "01", "MPSP", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpsp/01/2022")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_01_2022, result_to_dict["contraCheque"][0])
    
    def test_mpsp_02_2022(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpsp_02_2022.json", "r") as fp:
            expected_02_2022 = json.load(fp)

        files = [
            "src/output_test/sheets/MPSP-contracheques-02-2022.ods",
            "src/output_test/sheets/MPSP-indenizacoes-02-2022.ods",
        ]

        dados = data.Data("2022", "02", "MPSP", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpsp/02/2022")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_02_2022, result_to_dict["contraCheque"][0])

    def test_mpsp_03_2022(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpsp_03_2022.json", "r") as fp:
            expected_03_2022 = json.load(fp)

        files = [
            "src/output_test/sheets/MPSP-contracheques-03-2022.ods",
            "src/output_test/sheets/MPSP-indenizacoes-03-2022.ods",
        ]

        dados = data.Data("2022", "03", "MPSP", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpsp/03/2022")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_03_2022, result_to_dict["contraCheque"][0])

    def test_mpsp_08_2022(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpsp_08_2022.json", "r") as fp:
            expected_08_2022 = json.load(fp)

        files = [
            "src/output_test/sheets/MPSP-contracheques-08-2022.ods",
            "src/output_test/sheets/MPSP-indenizacoes-08-2022.ods",
        ]

        dados = data.Data("2022", "08", "MPSP", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpsp/08/2022")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_08_2022, result_to_dict["contraCheque"][0])
    
    def test_mpsp_01_2023(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpsp_01_2023.json", "r") as fp:
            expected_01_2023 = json.load(fp)

        files = [
            "src/output_test/sheets/MPSP-contracheques-01-2023.ods",
            "src/output_test/sheets/MPSP-indenizacoes-01-2023.ods",
        ]

        dados = data.Data("2023", "01", "MPSP", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpsp/01/2023")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_01_2023, result_to_dict["contraCheque"][0])
    
    def test_mpsp_07_2023(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_mpsp_07_2023.json", "r") as fp:
            expected_07_2023 = json.load(fp)

        files = [
            "src/output_test/sheets/MPSP-contracheques-07-2023.ods",
            "src/output_test/sheets/MPSP-indenizacoes-07-2023.ods",
        ]

        dados = data.Data("2023", "07", "MPSP", "src/output_test/sheets")
        dados = data.load(files, dados)
        result_data = parse(dados, "mpsp/07/2023")

        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected_07_2023, result_to_dict["contraCheque"][0])
