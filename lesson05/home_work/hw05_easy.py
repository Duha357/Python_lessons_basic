import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_dir(x): #Чтобы создать 9 папок, вызовем функцию и в ней пропишем число 9
    a = 1
    while a <= x:
        b = os.path.join(os.getcwd(), "dir_{}".format(a)) #Проверяем путь к директории
        try:
            os.mkdir(b) #Создаём папку в директории
            print("dir_{}, создана!".format(a))
        except FileExistsError:
            print("Такой файл уже существует!")
        a += 1

def remove_dir(x): #Чтобы удалить 9 папок, вызовем функцию и в ней пропишем число 9
    a = 1
    while a <= x:
        b = os.path.join(os.getcwd(), "dir_{}".format(a)) #Проверяем путь к директории
        try:
            os.rmdir(b) #Удаляем папку в директории
            print("dir_{}, удалена!".format(a))
        except FileExistsError:
            print("Такого файла нет в этой директории!")
        a += 1



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def demonstrate():
    a = os.path.join(os.getcwd()) #Проверяем путь к директории
    b = os.listdir(a) #Выставляем список файлов
    for i in b:
        print(i)



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def create_copy():
    a = os.path.realpath(__file__) #Проверяем путь к файлу
    b = a + ".bak" #Переименновываем будущую копию
    shutil.copy(a, b)
    print(a, "/n", b) #Выводим пути к файлам исходника и копии