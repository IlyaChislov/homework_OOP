class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_hw_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and grade in range(1,10):
            if course in lecturer.grades:
                lecturer.grades[course]+=[grade]
            else:
                lecturer.grades[course]=[grade]
    def median_rate(self):
        if len(self.grades)!=0:
            res=sum(map(sum, self.grades.values()))/len(self.grades)
            return res
    def __str__(self):
        return f'Имя {self.name}\nФамилия {self.surname}\nCредняя оценка за домашние задания: {self.median_rate()}\nКурсы в процессе изучения:{", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
    def comparison(self, other):
        if isinstance(other, Student):
            return (self.median_rate() > other.median_rate())
        else:
            return "Нельзя сравнивать"



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached=[]
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached=[]
        self.grades={}
    def median_rate(self):
        if len(self.grades)!=0:
            res=sum(map(sum, self.grades.values()))/len(self.grades)
            return res
    def __str__(self):
        return f'Имя {self.name}\nФамилия {self.surname}\nСредняя оценка за лекции: {self.median_rate()}'
    def comparison(self, other):
        if isinstance(other, Lecturer):
            return (self.median_rate() > other.median_rate())
        else:
            return "Нельзя сравнить"

def median_rate_of_students(students, course):
    res=0
    count=0
    for student in students:
        if course in student.grades.keys():
            res+=sum(student.grades[course])
            count+=len(student.grades[course])
    return round(res/count, 2)
def median_rate_of_lecturers(lecturers, course):
    res=0
    count=0
    for lecturer in lecturers:
        if course in lecturer.grades.keys():
            res+=sum(lecturer.grades[course])
            count+=len(lecturer.grades[course])
        return round(res/count)
first_student=Student('Sergey', 'Ivanov', 'male')
second_student=Student('Kirill', 'Andreev', 'male')
first_student.courses_in_progress=['Python', 'Java_Script', 'Data_Engineer']
first_student.finished_courses=['Java']
second_student.courses_in_progress=['Python', 'DevOps']
second_student.finished_courses=['Git']
first_reviewer=Reviewer('Ivan', "Khohkov")
second_reviewer=Reviewer('Ivan', "Khohkov")
first_reviewer.courses_attached=['Java', 'Python']
second_reviewer.courses_attached=['DevOps', 'Data_Engineer']
first_lecturer=Lecturer('Valentina', 'Asadova')
second_lecturer=Lecturer('Eduard', 'Stelmah')
first_lecturer.courses_attached=['Python', 'Java', 'Java_Script']
second_lecturer.courses_attached=['Python', 'DevOps', 'Data_Engineer', 'Java_Script']
first_reviewer.rate_hw(second_student, 'Python', 4)
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(second_student, 'Python', 5)
second_reviewer.rate_hw(first_student, 'Data_Engineer', 6)
second_reviewer.rate_hw(first_student, 'Java_Script', 3)
first_student.rate_hw_lec(second_lecturer, 'Date_Engineer', 7)
second_student.rate_hw_lec(first_lecturer, 'Python', 8)
second_student.rate_hw_lec(second_lecturer, 'Python', 9)
first_student.rate_hw_lec(second_lecturer, 'Java_Script', 9)

print(median_rate_of_students([first_student, second_student], 'Python'))
print(median_rate_of_students([first_lecturer, second_lecturer], 'Python'))


