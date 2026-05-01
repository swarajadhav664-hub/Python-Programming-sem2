# act 1
"""
Created on Fri May  1 22:37:31 2026

@author: swaranjali jadhav
"""

# 1. Calculate EMI using math module
def calculate_emi(loan_amount, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    emi = (loan_amount * monthly_rate * math.pow(1 + monthly_rate, months)) / \
          (math.pow(1 + monthly_rate, months) - 1)
    return emi

