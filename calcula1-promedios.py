from functools import partial
from more_itertools import iterate
#from datetime import datetime

# Define students list (replace with your actual student data)
students = [
    {"name": "Alice", "dob": "2000-01-01", "grades": [8.5, 7.8, 9.2, 8.7]},
    {"name": "Bob", "dob": "1998-12-31", "grades": [9.0, 8.5, 8.0, 9.5]},
    {"name": "Liz", "dob": "2000-03-10", "grades": [9.5, 8.8, 9.2, 9.7]},
    {"name": "Marc", "dob": "1999-10-11", "grades": [9.0, 9.5, 9.0, 9.5]},
    # Add more students here
]

def calculate_average(grades: tuple [0:3]):
    return sum(grades) / len(grades)

print("Subject: Challenge #22-2024 on *Higher Order Functions*")

# Calculate average grades using map and partial function
average_grade = map(partial(calculate_average), (student["grades"] for student in students))
#average_grades = map(partial(calculate_average), (student["grades"] for student in students))

print("Average Grade per Student:")
for student, grade in zip(students, average_grade):
    print(f"{student['name']}'s average grade: {grade:.2f}")

average_grade = map(partial(calculate_average), (student["grades"] for student in students))

def is_top_student(average_grade):
    return average_grade >= 9.0

print("")

# Filter top students based on average grades
top_students = list(filter(is_top_student, average_grade))
top_student_names = [student["name"] for student in students if student["name"] in top_students]

average_grade = map(partial(calculate_average), (student["grades"] for student in students))

print("Top students (average >= 9.0):", ", ".join(top_student_names))
for student, grade in zip(top_student_names, top_students):
    print("{student['name']}'s average grade: {grade:.2f}")

for i in top_students:
    print(i)


