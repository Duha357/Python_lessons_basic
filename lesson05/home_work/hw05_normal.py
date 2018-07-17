# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import sys
import os
import hw05_easy

print("Мы тут:", sys.argv) #Путь к текущей директории.

def help():
    print("1. Перейти в папку")
    print("2. Просмотреть содержимое текущей папки")
    print("3. Удалить папку")
    print("4. Создать папку")

def move_to_dir():
    a = input("Введите имя папки, в которую хотите переместиться: ")
    if not a:
        print("Вы не ввели имя папки!")
        return
    b = os.path.join(os.getcwd(), "{}".format(a))
    try:
        os.chdir(b) #Это не работает
        os.system("cd " + a) #И это не работает, просьба подсказать почему, пытался задать чтоб пользователь вводил
        # путь до папки, но chdir всё равно не переключает путь директории в командной строке
        print("Мы перемещены в папку {}!".format(a))
    except FileNotFoundError:
        print("Папки нет по этому пути!")

def delete_dir():
    a = input("Введите имя папки, которую хотите удалить: ")
    if not a:
        print("Вы не ввели имя папки!")
        return
    b = os.path.join(os.getcwd(), "{}".format(a))
    try:
        os.rmdir(b)
        print("Папка {} успешно удалена!".format(a))
    except FileExistsError:
        print("Папки {} нет в этой папке!".format(a))

def create_dir():
    a = input("Введите имя папки, которую хотите создать: ")
    if not a:
        print("Вы не ввели имя папки!")
        return
    b = os.path.join(os.getcwd(), "{}".format(a))
    try:
        os.mkdir(b)
        print("Папка {} успешно создана!".format(a))
    except FileExistsError:
        print("Папка {} уже существует!".format(a))

do = {
    "help": help,
    "1": move_to_dir,
    "2": hw05_easy.demonstrate, #Как мне объяснил наставник, это единственный скрипт, который можно импортировать.
    "3": delete_dir,
    "4": create_dir
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Такой функции не реализовано!")
        print("Введите help, для справки")