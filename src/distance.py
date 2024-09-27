def get_user_dict() -> dict:
    result = {}
    count = int(input("Введите количество элементов в словаре: "))
    if count <= 0:
        print("Количество не может быть меньше или равно 0!")
        return {}

    for el in range(count):
        key = input("Введите ключ: ")
        value_input = input("Введите значение: ")
        for item in value_input.split():
            if int(item) < 0:
                print("Расстояние не может быть отрицательным")
                return {}
        value = tuple(map(int, value_input.split()))
        result[key] = value
    return result

def calculate_distance(cities : dict) -> dict:
    if cities == {}:
        return {}
    distances = {}

    for i in cities:
        distances[i] = {}
        for j in cities:
            distances[i][j] = ( (cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2) ** 0.5
    return distances

def get_distances() -> dict:
    cities = get_user_dict()
    if cities == {}:
        return {}
    distances = calculate_distance(cities)

    return distances

def print_distance():
    if get_distances() != {}:
        print(get_distances())



