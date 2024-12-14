from math import pi, sqrt

class Figure:
    sides_count = 0
    def __init__(self, __color, *__sides):
        self.__color = list(__color)
        self.__sides = []
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return isinstance(r, int) and isinstance(g, int) and isinstance(b, int)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__( __color, *__sides)
        self.__sides = __sides
        self.__radius = self.__sides[0] / (2 * pi)

    def get_square(self):
        return pi * (self.__radius ** 2)


class Triangle(Figure):

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__sides = __sides
        self.half_meter = (1 / 2) * sum(__sides)

    def get_square(self):
        return sqrt(self.half_meter * (self.half_meter - self.__sides[0]) * (self.half_meter - self.__sides[1])\
                    * (self.half_meter - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__sides = __sides


    def get_sides(self):
        self.__sides = [self.__sides[0]] * self.sides_count
        return self.__sides

    def get_volume(self):
        v = self.__sides[0] ** 3
        return v

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())

circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



