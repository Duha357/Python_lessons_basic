
__author__ = 'Семериков Андрей Владимирович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

a = input("Введите любое число: ")
for i in a:
    print(i)
#Или ещё вот так, вроде работает:
a = int(input("Введите любое число: "))
b = list(str(a))
c = len(b)
d = 0
while d < c:
    print(b[d])
    d += 1



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input("Введите любое число №1: "))
b = int(input("Введите любое число №2: "))
c = 0
c = a
a = b
b = c
print("Теперь число №1 равно: ", a)
print("Теперь число №2 равно: ", b)



# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Введите возраст: "))
access = 0
if age >= 18:
    print("Доступ разрешен")
    access = True
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
    access = False
