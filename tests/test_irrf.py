import unittest
import irrf
from irrf import IrrfRate

class TestIrrf(unittest.TestCase):
    def test_taxFree(self):
        irrf_rate = IrrfRate(0,1800,0,0,100)
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