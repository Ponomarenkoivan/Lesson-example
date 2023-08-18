# Створити ієрархію класів для опису академії.
#
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
#
# Продумати архітектуру: реалізувати принципи ООП

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"


class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject):
        super().__init__(first_name, last_name, age)
        self.subject = subject

    def teach(self):
        return f"{self.get_full_name()} teaches the subject {self.subject}"


class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.get_full_name()} studies subjects"


class Subject:
    def __init__(self, name):
        self.name = name


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)


class Classroom:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True
        else:
            return False


math_teacher = Teacher("Ivan", "Petrenko", 35, "Math")
history_teacher = Teacher("Mariya", "Sidorenko", 40, "History")

student1 = Student("Oleksiy", "Ivanenko", 20, "A123")
student2 = Student("Anna", "Kovalenko", 19, "A456")

math_subject = Subject("Math")
history_subject = Subject("History")

academy = Academy("Banking Academy")

academy.add_teacher(math_teacher)
academy.add_teacher(history_teacher)
academy.add_student(student1)
academy.add_student(student2)
academy.add_subject(math_subject)
academy.add_subject(history_subject)

math_classroom = Classroom("Audience 101", 30)
history_classroom = Classroom("Audience 201", 25)

math_classroom.add_student(student1)
history_classroom.add_student(student2)

print(f"{math_teacher.get_full_name()} teaches the subject {math_subject.name}")
print(f"{history_teacher.get_full_name()} teaches the subject {history_subject.name}")

for student in academy.students:
    print(student.study())

print(f"{math_classroom.name} contains {len(math_classroom.students)} students")
print(f"{history_classroom.name} contains {len(history_classroom.students)} students")


print(Student.mro())
print(Teacher.mro())



