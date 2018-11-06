import unittest
import inss
from inss import InssRate

class TestInss(unittest.TestCase):
    def setUp(self):
        self.inss = inss.InssRate(0,3000,10)

    def test_inssInsideLimit(self):
        result = self.inss.calculate(2000)
        self.assertEqual(result, 200)

    def test_inssEdgeLimit(self):
        result = self.inss.calculate(3000)
        self.assertEqual(result, 300)
    
    def test_abovelimit(self):
        result = self.inss.calculate(4000)
        self.assertEqual(result, 300)

class TestSelectionInss(unittest.TestCase):
    def setUp(self):
        self.table = [
            InssRate(0,1000,9),
            InssRate(1001,2000,10),
            InssRate(2001,3000, 11)
        ]

    
    def test_loadAnyone(self):
        inssRate = inss.get_Inss_by_value(1000, self.table)
        self.assertEqual(9, inssRate.rate)

    def test_loadAboveLimit(self):
        inssRate = inss.get_Inss_by_value(5000, self.table)
        self.assertEqual(11, inssRate.rate)

class TestReadingInss(unittest.TestCase):
    def test_loadFromDefault(self):
        table = inss.load_inss()
        self.assertEqual(len(table), 3)

if __name__ == "__main__":
    unittest.main()