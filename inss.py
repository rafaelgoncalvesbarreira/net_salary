import csv

class InssRate:
    def __init__(self, min=0, max=0, rate=0):
        self.min=min
        self.max = max
        self.rate =rate
    
    def calculate(self, value):
        base = value if value< self.max else self.max
        return base * self.rate / 100

def load_inss(csv_file_path='inss.csv'):
    field_names=['min', 'max', 'rate']
    insss=[]
    with open(csv_file_path) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=field_names)
        for row in reader:
            o = InssRate(row['min'], row['max'], row['rate'])
            insss.append(o)
    return insss

def get_Inss_by_value(base_inss, list_inss):
    list_inss.sort(key= lambda x: x.rate)
    for inss in list_inss:
        if inss.min <= base_inss <= inss.max:
            return inss
    return list_inss[-1]