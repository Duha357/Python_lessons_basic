# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = 1 #Введём начальные значения
    b = 1
    c = 2
    while c < n: #Отсчитываем до начала отчёта
        c = a + b
        a = a + b - a
        b = c
    print(n)
    print(c)
    while n < m: #Считаем числа до конечного
        n = a + b
        a = a + b - a
        b = n
        print(n)
    return



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    a = []
    while len(origin_list) > 0:
        b = origin_list[0]
        for i in origin_list:
            if i <= b: #Зацикливаем проверку каждого следующего числа, не больше ли оно предыдущего
                b = i #Если следующее число меньше, оно поднимается выше - пузырьком
        a.append(b)
        origin_list.remove(b)
    return a

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def a(c, d):
    b = []
    for i in d:
        if i != c: #Проверка на отфильтровывание заданного аргумента
            b.append(i)
    return b



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def a(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x2 - x1 == x4 - x3 and y2 - y1 == y4 - y3) or (x2 - x1 == x3 - x4 and y2 - y1 == y3 - y4) or\
            (x3 - x1 == x4 - x2 and y3 - y1 == y4 - y2) or (x3 - x1 == x2 - x4 and y3 - y1 == y2 - y4) or\
            (x4 - x1 == x3 - x2 and y4 - y1 == y3 - y2) or (x4 - x1 == x2 - x3 and y4 - y1 == y2 - y3):
        return True #Проверили все возможные равенства сторон
    else:
        return False