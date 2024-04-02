from abc import ABC, abstractmethod
from math import pi, sqrt


class Figure(ABC):     # абстрактный класс фигуры
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass


class Circle(Figure):   # круг
    def __init__(self, *args):
        if len(args) == 1:
            self.radius = args[0]
            self.name = 'Circle'
        else:
            raise ValueError("1 argument is required. ", len(args), " was given.")

    def area(self):
        return round(pi * self.radius ** 2)

    def print_area(self):
        print(f'Area of {self.name} is {self.area()}')


class Triangle(Figure):    # треугольник
    def __init__(self, *args):
        if len(args) == 3:  # проверка количества аргументов
            self.side1 = args[0]
            self.side2 = args[1]
            self.side3 = args[2]
            self.name = 'Triangle'
        else:
            raise ValueError("3 arguments is required. ", len(args), " was given.")
        if self.side1 + self.side2 < self.side3 or self.side1 + self.side3 < self.side2 \
                or self.side2 + self.side3 < self.side1:    # проверка существования треугольника
            raise ValueError(f'Triangle with sides {self.side1}, {self.side2}, {self.side3} does not exist.')

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return round(sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)), 2)

    def is_right_triangle(self):
        return self.side1 == self.side2 and self.side2 == self.side3

    def is_rectangular_triangle(self):
        if not self.is_right_triangle():
            sides = [self.side1, self.side2, self.side3]
            sides.sort(reverse=True)
            return sides[0] ** 2 == sides[1] ** 2 + sides[2] ** 2

    def print_area(self):
        print(f'Area of {self.name} is {self.area()}')
