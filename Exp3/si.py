#experiment no.3 code 2
"""
Created on Tue Feb 17 12:50:36 2026

@author: swaranjali jadhav
"""
def simple_interest(principle,rate,time):
     si = (principle*rate*time)/100
     return si
 #Taking input from the user 
p= float(input("Enter principle amount:"))
r = float(input("Enter rate of intrest:"))
t = float(input("Enter time (in years):"))
 #Function call
intrest = simple_interest(p,r,t)
print("simple intrest is:",intrest)
 