class Person:
    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Person):
    def __init__(self, first_name, last_name, birth_date, gender, subject_taught):
        super().__init__(first_name, last_name, birth_date, gender)
        self.subject_taught = subject_taught

    def teach(self):
        print(f"{self.get_full_name()} is teaching {self.subject_taught}")


class Student(Person):
    def __init__(self, first_name, last_name, birth_date, gender, student_id):
        super().__init__(first_name, last_name, birth_date, gender)
        self.student_id = student_id
        self.courses_taken = []

    def enroll(self, subject):
        self.courses_taken.append(subject)
        print(f"{self.get_full_name()} has enrolled in {subject}.")

    def list_courses(self):
        print(f"{self.get_full_name()} is taking the following courses: {', '.join(self.courses_taken)}")


class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects_offered = []

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)
            print(f"{teacher.get_full_name()} has joined {self.name} as a teacher.")
        else:
            print("Invalid teacher object.")

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"{student.get_full_name()} has joined {self.name} as a student.")
        else:
            print("Invalid student object.")

    def add_subject(self, subject):
        if isinstance(subject, Subject):
            self.subjects_offered.append(subject)
            print(f"{subject.name} ({subject.code}) has been added to the courses offered by {self.name}.")
        else:
            print("Invalid subject object.")



my_academy = Academy("My University")

math_teacher = Teacher("John", "Doe", "01-01-1980", "Male", "Mathematics")
my_academy.add_teacher(math_teacher)

john_student = Student("Jane", "Doe", "01-01-2000", "Female", "2022001")
my_academy.add_student(john_student)

math_subject = Subject("Mathematics 101", "MATH101")
my_academy.add_subject(math_subject)

john_student.enroll(math_subject)

print(f"Subjects offered by {my_academy.name}: {[subject.name for subject in my_academy.subjects_offered]}")

math_teacher.teach()