from collections import namedtuple

Student = namedtuple("Student", ['name', 'major', 'gpa'])

def load_students(file_name):
    """Read and sort the factors in the file. The argument should be a file name."""
    with open(file_name) as file:
        student_group = []

        for line in file:
            line = line.strip()
            parts = line.split(",")
            student = Student(parts[0], parts[1], float(parts[2]))
            student_group.append(student)
        return student_group

def highest_gpa(students):
    """Return the student who has the highest GPA. The argument should be a list."""
    highest_student = students[0]
    for student in students:
        if student.gpa > highest_student.gpa:
            highest_student = student
    return highest_student

def average_gpa(students):
    """Return the average GPA. The argument should be a list."""
    total_gpa = 0
    for student in students:
        total_gpa += student.gpa
    return total_gpa / len(students)

def count_majors(students):
    """Return the number of each major. The argument should be a list."""
    major_num = {}
    for student in students:
        if student.major not in major_num:
            major_num[student.major] = 1
        else:
            major_num[student.major] += 1
    return major_num

def honor_students(students):
    """Return honor students(who with GPA no lower than 3.7). The argument should be a list."""
    honors = []
    for student in students:
        if student.gpa >= 3.7:
            honors.append(student)
    return honors
