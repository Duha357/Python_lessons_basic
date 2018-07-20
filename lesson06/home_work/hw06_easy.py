import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.AB = round(math.sqrt(int(math.fabs(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((x1 - x3) ** 2) + ((y1 - y3) ** 2)))), 2)

    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return self.perimetr

    def vysota(self):
        self.x4 = (x1 - x3) / 2  #Находим координаты середины отрезка CA
        self.y4 = (x1 - y3) / 2
        self.h = round(math.sqrt(int(math.fabs(((x4 - x2) ** 2) + ((y4 - y2) ** 2)))), 2) #Находим высоту треугольника
        return self.h

    def ploshad(self):
        self.polovina_osnovania = self.CA / 2 #Находим длинну половины основания
        self.ploshad = self.polovina_osnovania * self.h
        return self.ploshad

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapeze():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def storoni(self):
        self.AB = round(math.sqrt(int(math.fabs(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))), 2)
        self.CD = round(math.sqrt(int(math.fabs(((x4 - x3) ** 2) + ((y4 - y3) ** 2)))), 2)
        self.DA = round(math.sqrt(int(math.fabs(((x1 - x4) ** 2) + ((y1 - y4) ** 2)))), 2)
        return self.AB, self.BC, self.CD, self.DA

    def proverka(self):
        if self.BC == self.DA and self.AB != self.CD or self.BC != self.DA and self.AB == self.CD:
            print("Трапеция равнобедренная!")
        else:
            print("Трапеция не равнобедренная!")

    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CD + self.DA)
        return self.perimetr

    def ploshad(self):
        if self.BC == self.DA and self.AB != self.CD:
            self.katet = int(math.fabs(self.AB - self.CD)) #Делаем катет бокового треугольника трапеции
            self.h = round(math.sqrt(int((self.BC ** 2) - (self.katet ** 2))), 2) #Находим высоту трапеции по Пифагору
            self.polusumma_vershini_i_osnovania = int(self.AB + self.CD) / 2  # Находим полусумму вершины и основания
            self.ploshad = self.polusumma_vershini_i_osnovania * self.h
            return self.ploshad
        elif self.BC != self.DA and self.AB == self.CD:
            self.katet = int(math.fabs(self.BC - self.DA))  # Делаем катет бокового треугольника трапеции
            self.h = round(math.sqrt(int((self.AB ** 2) - (self.katet ** 2))), 2)  # Находим высоту трапеции по Пифагору
            self.polusumma_vershini_i_osnovania = int(self.BC + self.DA) / 2  # Находим полусумму вершины и основания
            self.ploshad = self.polusumma_vershini_i_osnovania * self.h
            return self.ploshad