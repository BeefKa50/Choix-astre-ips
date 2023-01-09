import numpy as np
import pandas as pd
from functions import initializeStudent
from student import Student
df = pd.read_csv(r'data\data.csv')

students = []

for index, row in df.iterrows():
    student = Student()
    initializeStudent(student,row)
    students.append(student)

for student in students:
    print(vars(student))

print("-----------------------------------------------------------------")
print(vars(students[2]))
print(students[2].answersAsArray())