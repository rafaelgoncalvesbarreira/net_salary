import csv

class IrrfRate:
    def __init__(self, min=0, max=0, rate=0, deduction=0, dependents_reduction=0):
        self.min=min
        self.max = max
        self.rate =rate
        self.deduction = deduction
        self.dependents_reduction = dependents_reduction
    
    def calculate(self, base_value, dependents=0):
        value = 0
        if self.min <= base_value <= self.max:
            base = base_value if dependents==0 else base_value - (dependents * self.dependents_reduction)
            rate = base * self.rate / 100
            value = rate - self.deduction
        return value

def load_dependent_reduction(csv_file_path='dependents.csv'):
    reduction = 0
    with open(csv_file_path) as csvfile:
        lines = csvfile.readlines()
        reduction = float(lines[1])
    return reduction

def load_irrf(csv_file_path='irrf.csv', dependents_reduction=0):
    field_names=['min', 'max', 'rate', 'deduction']
    irrfs=[]
    with open(csv_file_path) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=field_names)
        for row in reader:
            o = IrrfRate(row['min'], row['max'], row['rate'], row['deduction'], dependents_reduction)
            irrfs.append(o)
    return irrfs


def get_irrf_by_value(base_irrf, list_irrf):
    list_irrf.sort(key= lambda x: x.rate)
    for irff in list_irrf:
        if irff.min <= base_irrf <= irff.max:
            return irff
    return list_irrf[-1]
