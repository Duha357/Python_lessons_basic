# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import sys
import os
print("sys.argv = ", sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создать копию файла")
    print("rm <file_name> - удалить файл ")
    print("cd <full_path> - изменить директорию")
    print("ls - отобразить полный путь текущей директории")
def make_dir():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print("директория {} создана".format(dir_name))
    except FileExistsError:
        print("директория {} уже создана".format(dir_name))
def ping():
    print("pong")
def create_copy():
    if not file_name:
        print("Вы забыли имя указать")
            return
    a = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
    try:
        b = a + ".bak"  # Переименновываем будущую копию
        shutil.copy(a, b)
        print(a, "/n", b)  # Выводим пути к файлам исходника и копии
    except FileExistsError:
        print("Неуверенность, похоже это не файл")

def delete_file():
    if not file_name:
        print("Вы забыли имя указать")
        return

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
def we_here():
    print(os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": create_copy,
    "rm": delete_file,
    "cd": move_to_dir,
    "ls": we_here
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