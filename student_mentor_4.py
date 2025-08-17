class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # ключ - курс, значение - список оценок

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
           course in self.courses_in_progress and \
           course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 1)
        return 0

    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {in_progress}\n"
                f"Завершенные курсы: {finished}")

    # Сравнение студентов по средней оценке
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 1)
        return 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade()}")

    # Сравнение лекторов по средней оценке
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and \
           course in self.courses_attached and \
           course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# --- Создание объектов ---
student1 = Student('Ruoy', 'Eman', 'Ж')
student2 = Student('Alex', 'Smith', 'М')

lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('John', 'Doe')

reviewer1 = Reviewer('Anna', 'Bell')
reviewer2 = Reviewer('Mike', 'Jones')

# --- Настройка курсов ---
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student2.courses_in_progress = ['Python', 'Git']
student2.finished_courses = ['Введение в программирование']

lecturer1.courses_attached = ['Python', 'Git']
lecturer2.courses_attached = ['Python', 'Git']

reviewer1.courses_attached = ['Python', 'Git']
reviewer2.courses_attached = ['Python', 'Git']

# --- Проставляем оценки студентами лекторам ---
student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Git', 9)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Git', 9)

# --- Проставляем оценки проверяющими студентам ---
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Git', 9)

# --- Функции для подсчета средней оценки ---
def avg_hw_for_course(students, course_name):
    total = 0
    count = 0
    for student in students:
        if course_name in student.grades:
            total += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    return round(total / count, 1) if count > 0 else 0

def avg_lecture_for_course(lecturers, course_name):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total += sum(lecturer.grades[course_name])
            count += len(lecturer.grades[course_name])
    return round(total / count, 1) if count > 0 else 0

# --- Списки для функций ---
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

# --- Вызов функций ---
print("Средняя оценка студентов за курс Python:", avg_hw_for_course(students, 'Python'))
print("Средняя оценка студентов за курс Git:", avg_hw_for_course(students, 'Git'))
print("Средняя оценка лекторов за курс Python:", avg_lecture_for_course(lecturers, 'Python'))
print("Средняя оценка лекторов за курс Git:", avg_lecture_for_course(lecturers, 'Git'))

# --- Вывод информации о всех объектах ---
for obj in [student1, student2, lecturer1, lecturer2, reviewer1, reviewer2]:
    print()
    print(obj)