# exp.7 act 2
"""
Created on Fri May  1 22:07:23 2026

@author: swaranjali jadhav
"""

# 1. Employee class that calculates salary with bonus
class Employee:
    def __init__(self, name, base_salary, bonus):
        self.name = name
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

