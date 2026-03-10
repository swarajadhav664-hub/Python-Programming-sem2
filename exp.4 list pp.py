# --*-
"""
Created on Tue Mar 10 13:03:02 2026



@author:swaranjali jadhav
"""
#Taking list input from the users
n = int(input("enter numbers of element:"))
numbers = []
for i in range (n):
    num = int(input(f"Enter element {i+1}:"))
    numbers.append(num)
#Calculating sum and average
total = sum(numbers)
average = total /n if n > 0 else 0
print("List.",numbers)
print("sum of elements:",total)
print("average of elements:",average )