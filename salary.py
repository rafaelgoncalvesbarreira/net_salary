import irrf
import inss

class ConfigurationData:
    def __init__(self):
        self.irrf_table =[]
        self.inss_table=[]

def calculate_net_salary(salary=0, number_dependents=0, config=ConfigurationData()):
    inss_rate = inss.get_Inss_by_value(salary, config.inss_table)
    inss_value = inss_rate.calculate(salary) 

    base_irrf = salary - inss_value
    irrf_rate = irrf.get_irrf_by_value(base_irrf, config.irrf_table)
    irrf_value = irrf_rate.calculate(base_irrf, number_dependents)

    return salary - (inss_value + irrf_value)

def calculate_net_salaries(salaries=[], number_dependents=0, config=ConfigurationData()):
    result = []
    for salary in salaries:
        result.append((salary,calculate_net_salary(salary, number_dependents, config)))
    
    return result
    

def load_data():
    config = ConfigurationData()
    config.inss_table = inss.load_inss()
    dependent_reduction = irrf.load_dependent_reduction()
    config.irrf_table = irrf.load_irrf(dependents_reduction=dependent_reduction)
    return config;

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('salaries', type=float, help="List of base salaries", nargs='+')
    parser.add_argument("-d", "--dependents", type=int, help="number of legal dependents", default=0)
    #parser.add_argument("-m","--money", type=float, help="the money invested", required=True)
    #parser.add_argument("-i", "--interest", type=float, help="interest per month", required=True)
    #parser.add_argument("-t", "--time", type=int, help="months", required=True)
    args = parser.parse_args()

    config = load_data()
    result = calculate_net_salaries(args.salaries, args.dependents, config)
    for r in result:
        print(f'salary base: {r[0]:.2f} -> net: {r[1]:.2f}')