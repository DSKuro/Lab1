import math

def input_circle() -> tuple:
    radius = int(input("Введите радиус: "))
    if radius <= 0:
        print("Радиус не может быть неположительным!")
        return 0, 0
    point = tuple(map(int, input("Введите точку: ").split()))
    return radius, point

def in_circle(radius : int, point: tuple) -> str:
    distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
    return str(distance <= radius)

def get_s(radius: int) -> float:
    pi = round(math.pi, 7)
    return round((pi * (radius ** 2)), 4)

def get_answer(radius: int, point: tuple):
    s = get_s(radius)
    print("S круга: " + str(s))
    print("Точка лежит в/на круге: " + in_circle(radius, point))

def print_circle():
    radius, point = input_circle()
    if radius == 0 and point == 0:
        return
    get_answer(radius, point)
