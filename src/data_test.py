import data
import unittest


class TestData(unittest.TestCase):
    # Usando como exemplo MPPI, que não possui dados de indenizações em 2021
    def test_validate_existence_mppi_2021(self):
        STATUS_DATA_UNAVAILABLE = 4
        with self.assertRaises(SystemExit) as cm:
            dados = data.Data("2021", "01", "MPPI", "src/output_test/sheets/")
            dados.validate()
        self.assertEqual(cm.exception.code, STATUS_DATA_UNAVAILABLE)
 
    def test_validate_existence_mpsp_2021(self):
        # Sem dados para o MPSP em 2021
        STATUS_DATA_UNAVAILABLE = 4
        with self.assertRaises(SystemExit) as cm:
            dados = data.Data("2021", "01", "MPSP", "src/output_test/sheets/")
            dados.validate()
        self.assertEqual(cm.exception.code, STATUS_DATA_UNAVAILABLE)

if __name__ == "__main__":
    unittest.main()