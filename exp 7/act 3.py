# exp 7 act 3
"""
Created on Fri May  1 22:12:18 2026

@author: swaranjali jadhav
"""

# 2. Student class that calculates grade
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        elif self.marks >= 50:
            return 'D'
        else:
            return 'F'
