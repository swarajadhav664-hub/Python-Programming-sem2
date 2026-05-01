# exp 10 act 3
"""
Created on Fri May  1 22:56:50 2026

@author:swaranjali jadhav
"""

# 3. Student Result Calculator App
def student_result():
    marks = []
    for i in range(5):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    total = sum(marks)
    average = total / len(marks)

    print("Total Marks:", total)
    print("Average:", round(average, 2))

    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 60:
        print("Grade: C")
    else:
        print("Grade: D")

