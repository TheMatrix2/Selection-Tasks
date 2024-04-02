# pip install pytest
import pytest
from Geometry import *


class TestCircle:
    def test_circle_creation(self):
        try:
            circle = Circle(5)
        except ValueError:
            pytest.fail("Circle initialization failed unexpectedly.")

        with pytest.raises(ValueError):
            circle = Circle(3, 5)
        with pytest.raises(ValueError):
            circle = Circle()

    def test_circle_area1(self):
        circle = Circle(5)
        assert circle.area() == round(25 * pi)

    def test_circle_area2(self):
        circle = Circle(0.4)
        assert circle.area() == round(0.16 * pi)


class TestTriangle:
    def test_triangle_creation(self):
        try:
            triangle = Triangle(3, 4, 5)
        except ValueError:
            pytest.fail("Triangle initialization failed unexpectedly.")

        with pytest.raises(ValueError):
            triangle = Triangle(7, 8)
        with pytest.raises(ValueError):
            triangle = Triangle(1, 2, 3, 4)

    def test_triangle_exists(self):
        with pytest.raises(ValueError):
            triangle = Triangle(0.5, 10, 5)

    def test_triangle_area(self):
        triangle = Triangle(5, 8, 10)
        assert triangle.area() == round(19.81004, 2)

    def test_triangle_is_right(self):
        triangle = Triangle(5, 5, 5)
        assert triangle.is_right_triangle() == True
