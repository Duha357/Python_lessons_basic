# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    if ndigits <= 0: #Проверяем на правильность ввода округления
        print("Количество знаков после запятой не должно быть меньше или ровняться нулю!")
    number = str(number)
    a = number.split(".") #Делим число на цифры до и после точки
    b = a[1]
    c = a[0]
    if len(b) <= ndigits: #Проверяем, не меньше ли и не равно ли число количеству знаков после запятой
        b = int(b)
        return "{}{}{}".format(a[0], ".", b)
    else:
        while len(str(b)) == ndigits + 1: #Доводим кол-во знаков до нужного
            b = int(b) // 10
        if int(b) % 10 <= 5: #Проверка на округление до 5-ти
            b = int(b) // 100
            if len(str(b)) == ndigits + 1: #Проверяем увеличение целой части числа
                c = int(c) + 1
                b = 0
        else: #Проверка на округление от 5-ти
            b = int(b) // 100 + 1
            if len(str(b)) == ndigits + 1:
                c = int(c) + 1
                b = 0
        return "{}{}{}".format(c, ".", b)
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if ticket_number > 6 and ticket_number < 6: #Проверка на соответствие это легко убрать в коментарии, чтоб не print'ить
        print("Номер не является шестизначным!")
    ticket_number = list(map(int, list(str(ticket_number)))
    if sum(ticket_number[:3]) == sum(ticket_number[3:]): #Проверка суммы правой и левой половины
        return True
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
