import unittest
import irrf
from irrf import IrrfRate

class TestIrrf(unittest.TestCase):
    def test_taxFree(self):
        irrf_rate = IrrfRate(0,1800,0,0,100)
        irrf_value = irrf_rate.calculate(1500)
        self.assertEqual(irrf_value,0)
    
    def test_wrongRating(self):
        irrf_rate = IrrfRate(1800,3500,10,100,100)
        irrf_value = irrf_rate.calculate(1500)
        self.assertEqual(irrf_value,0)
    
    def test_payTaxWithoutDependent(self):
        irrf_rate = IrrfRate(1800,3500,10,100,100)
        irrf_value = irrf_rate.calculate(3000)
        self.assertEqual(irrf_value, 200)
    
    def test_payTaxWithDependents(self):
        irrf_rate = IrrfRate(1800,3500,10,100,100)
        irrf_value = irrf_rate.calculate(3000,1)
        self.assertEqual(irrf_value, 190)

class TestLoadInss(unittest.TestCase):
    def setUp(self):
        self.table = [
            IrrfRate(0,1800,0,0,100),
            IrrfRate(1801,3500,10,100,100),
            IrrfRate(3501,999999,20,300,100)
        ]
    
    def test_load_anyone(self):
        irrf_rate = irrf.get_irrf_by_value(3000,self.table)
        self.assertEqual(irrf_rate.rate, 10)


if __name__ == "__main__":
    unittest.main()