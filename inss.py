import csv
from decimal import Decimal

class InssRate:
    def __init__(self, min=0, max=0, rate=0):
        self.min= Decimal(min)
        self.max = Decimal(max)
        self.rate =Decimal(rate)
    
    def calculate(self, value):
        base = value if value< self.max else self.max
        value = Decimal(base * self.rate / 100)
        return round(value,2)

def load_inss(csv_file_path='inss.csv'):
    insss=[]
    with open(csv_file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            o = InssRate(Decimal(row['min']), Decimal(row['max']), Decimal(row['rate']))
            insss.append(o)
    return insss

def get_Inss_by_value(base_inss, list_inss):
    list_inss.sort(key= lambda x: x.rate)
    for inss in list_inss:
        if inss.min <= base_inss <= inss.max:
            return inss
    return list_inss[-1]