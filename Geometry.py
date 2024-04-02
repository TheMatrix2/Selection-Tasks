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
        if len(args) == 3:
            self.side1 = args[0]
            self.side2 = args[1]
            self.side3 = args[2]
            self.name = 'Triangle'
        else:
            raise ValueError("3 arguments is required. ", len(args), " was given.")

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_triangle(self):
        return self.side1 == self.side2 and self.side2 == self.side3

    def print_area(self):
        print(f'Area of {self.name} is {self.area()}')


class Rectangle(Figure):    # прямоугольник
    def __init__(self, *args):
        if len(args) == 2:
            self.width = args[0]
            self.height = args[1]
            self.name = 'Rectangle'
        else:
            raise ValueError(f"2 arguments is required. {len(args)} was given.")

    def area(self):
        return self.width * self.height

    def is_square(self):
        return self.width == self.height

    def print_area(self):
        print(f'Area of {self.name} is {self.area()}')
