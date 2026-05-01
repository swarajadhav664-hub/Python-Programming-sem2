# exp. 3 act 3
"""
Created on Fri May  1 22:26:23 2026

@author: swaranjali jadhav 
"""

# 3. Multiplication tables from 1 to 10
def multiplication_tables():
    for i in range(1, 11):
        print(f"\nTable of {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
