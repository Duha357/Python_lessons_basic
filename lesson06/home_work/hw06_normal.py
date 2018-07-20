# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, class_room):
        self.class_room = {
            "class_num": int(class_room.split()[0]),
            "class_letter": class_room.split()[1]
        }

    def get_name(self):
        return str(self.class_room["class_num"]) + " " + self.class_room["class_letter"]

class Person:
    def __init__(self, name, surname, second_name):
        self.name = name
        self.surname = surname
        self.second_name = second_name

    def get_full_name(self):
        return self.surname + " " + self.name + " " + self.second_name


class Student(Person):
    def __init__(self, name, surname, second_name, class_room, father, mother):
        Person.__init__(self, name, surname, second_name)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.father.get_full_name(), self.mother.get_full_name()


class Teacher(Person):
    def __init__(self, name, surname, second_name, classes, subject):
        Person.__init__(self, name, surname, second_name)
        self.classes = classes
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.classes


class_rooms = ["1 А", "2 Б", "3 В"]
father = [Person("Иван", "Сидоров", "Игоревич"),
            Person("Игорь", "Иванов", "Александрович"),
            Person("Николай", "Петров", "Александрович")]
mother = [Person("Татьяна", "Сидорова", "Максимовна"),
            Person("Ирина", "Иванова", "Александровна"),
            Person("Светлана", "Петрова", "Николаевна")]
students = [Student("Александр", "Иванов", "Игоревич", class_rooms[0], father[1], mother[1]),
            Student("Петр", "Сидоров", 'Иванович', class_rooms[1], father[0], mother[0]),
            Student("Иван", "Петров", 'Николаевич', class_rooms[1], father[2], mother[2]),
            Student("Алексей", "Иванов", "Игоревич", class_rooms[2], father[1], mother[1]),
            Student("Евгений", "Сидоров", 'Иванович', class_rooms[2], father[0], mother[0]),
            Student("Андрей", "Петров", 'Николаевич', class_rooms[2], father[2], mother[2])]
teachers = [Teacher("Иван", "Сидоров", "Игоревич", [class_rooms[0], class_rooms[1], class_rooms[2]], 'Математика'),
            Teacher("Игорь", "Иванов", "Александрович", [class_rooms[1], class_rooms[2]], 'История'),
            Teacher("Николай", "Петров", "Александрович", class_rooms[2], 'Английский')]

#for num, School in enumerate(class_rooms, start=1): #Не хватило времени
#    print("Все классы: {}) {}".format(num, School.get_name()))

for num, Student in enumerate(students, start=1):
    print("Все ученики в классах: {}) {} {}".format(num, Student.get_class_room(), Student.get_full_name()))

#На реализацию списка всх предметов ученика не хватило времени

for num, Parents in enumerate(students, start=1):
    print("Родители всех учеников: {}) Ученик: {} Родители: {}".format(num, Student.get_full_name(), Parents.get_parents()))

for num, Teacher in enumerate(teachers, start=1):
    print("Список учителей: {}) Учитель: {} Препадаёт в классе: {}".format(num, Teacher.get_full_name(), Teacher.get_classes()))