# exp.3 act 1
"""
Created on Fri May  1 22:20:08 2026

@author: swaranjali jadhav
"""

# 1. Nested loops to print item numbers repeatedly (receipt copies)
def print_receipts(items, copies):
    for copy in range(1, copies + 1):
        print(f"\nReceipt Copy {copy}:")
        for item in range(1, items + 1):
            print(f"Item {item}")

