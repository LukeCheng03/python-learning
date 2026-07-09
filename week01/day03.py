from collections import namedtuple

Student = namedtuple("Student", ['name', 'major', 'gpa'])

Luke = Student('Luke', 'Quantitative Econ', 3.6)
Alice = Student('Alice', 'Drama', 3.8)
Bob = Student('Bob', 'Literature', 3.5)
students = [Luke, Alice, Bob]

def highest_gpa(students):
    highest_score = 0
    highest_student = ''
    for student in students:
        if student.gpa > highest_score:
            highest_score = student.gpa
            highest_student = student
    return highest_student

print(highest_gpa(students))
