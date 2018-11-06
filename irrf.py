import csv

class IrrfRate:
    def __init__(self, min=0, max=0, rate=0, deduction=0, dependents_reduction=0):
        self.min=min
        self.max = max
        self.rate =rate
        self.deduction = deduction
        self.dependents_reduction = dependents_reduction
    
    def calculate(self, base_value, dependents=0):
        base = base_value if dependents==0 else base_value - (dependents * self.dependents_reduction)
        rate = base * self.rate / 100
        value = rate - self.deduction
        return value