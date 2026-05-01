

#exp.6 act 3
"""
Created on Tue Mar 24 13:15:54 2026

@author: swaranjali jadhav
"""
file = open("complaints.txt", "w")
file.write("Late service\nPoor quality\nDelay in response")
file.close()

file = open("complaints.txt", "r")
data = file.read()
print("Complaints:\n", data)
file.close() 