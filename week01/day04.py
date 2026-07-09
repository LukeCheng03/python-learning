from collections import namedtuple

Student = namedtuple("Student", ['name', 'major', 'gpa'])

def load_students(file_name):
    with open(file_name) as file:
        student_group = []

        for line in file:
            line = line.strip()
            parts = line.split(",")
            student = Student(parts[0], parts[1], float(parts[2]))
            student_group.append(student)
        return student_group

def highest_gpa(students):
    highest_student = students[0]
    for student in students:
        if student.gpa > highest_student.gpa:
            highest_student = student
    return highest_student

print(highest_gpa(load_students("week01/students.txt")))
