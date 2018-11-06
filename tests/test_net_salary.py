import unittest
import salary

class TestNetSalary(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.config = salary.load_data()

    def test_calculateOne(self):
        real_salary = salary.calculate_net_salary(3000, config=self.config)
        self.assertEqual(real_salary, 2612.55)
    
    def test_calculateWith2Dependent(self):
        real_salary = salary.calculate_net_salary(3000, number_dependents=2, config=self.config)
        self.assertEqual(real_salary, 2640.99)
    
    def test_multipleSalaries(self):
        data = [
            (3000,2612.55),
            (3300,2851.25),
            (4000,3380.80),
            (4500,3740.01),
            (5000,4084.88),
            (5500,4418.24),
            (6000,4768.85)
        ]

        input = [x[0] for x in data]
        
        
        results = salary.calculate_net_salaries(input, config=self.config)

        for i,result in enumerate(results):
            self.assertEqual(result, data[i])




if __name__ == "__main__":
    unittest.main()