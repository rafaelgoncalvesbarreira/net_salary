import os
import csv

inss=[]
irrf=[]
dependent_discount = 0

def load_inss():
    field_names=['min', 'max', 'rate']
    with open('inss.csv') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=field_names)
        for row in reader:
            

def load_irrf():
    pass

def load_dependents():
    pass

