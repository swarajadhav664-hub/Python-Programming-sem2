# exp. 3 act 2
"""
Created on Fri May  1 22:24:17 2026

@author: swaranjali jadhav
"""

# 2. Function to calculate EMI
def calculate_emi(loan_amount, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)  # Convert % to monthly decimal
    months = years * 12

    if monthly_rate == 0:
        return loan_amount / months

    emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)
    return emi
