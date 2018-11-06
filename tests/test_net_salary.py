import unittest
import salary
from decimal import Decimal

class TestNetSalary(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.config = salary.load_data()

    def test_calculateOne(self):
        real_salary = salary.calculate_net_salary(3000, config=self.config)
        self.assertEqual(real_salary, round(Decimal(2612.55),2))
    
    def test_calculateWith2Dependent(self):
        real_salary = salary.calculate_net_salary(3000, number_dependents=2, config=self.config)
        self.assertEqual(real_salary, round(Decimal(2640.99),2))
    
    def test_multipleSalaries(self):
        data = [
            (3000,round(Decimal(2612.55),2)),
            (3300,round(Decimal(2851.25),2)),
            (4000,round(Decimal(3380.80),2)),
            (4500,round(Decimal(3740.00),2)),
            (5000,round(Decimal(4084.88),2)),
            (5500,round(Decimal(4418.24),2)),
            (6000,round(Decimal(4769.11),2))
        ]

        input = [x[0] for x in data]
        
        
        results = salary.calculate_net_salaries(input, config=self.config)

        for i,result in enumerate(results):
            self.assertEqual(result, data[i])




if __name__ == "__main__":
    unittest.main()