def user_input() -> tuple:
    string = input("Введите любимые фильмы: ")
    delim = input("Введите разделитель: ")
    return string, delim

def get_positions(films : str, delimeter : str) -> list:
    delimeter_position = []
    for i in range(len(films)):
        if films[i] == delimeter:
            delimeter_position.append(i)

    return delimeter_position

def get_movies(films : str, delimeters : list) -> list:
    movies = list()
    movies.append(films[:delimeters[0]])
    movies.append(films[delimeters[-1] + 2:])
    movies.append(films[delimeters[0] + 2 : delimeters[1]])
    movies.append(films[delimeters[-4] + 2 : delimeters[-3]])

    return movies

def print_movies():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    default_delim = ","
    string, delim = user_input()
    if string == "":
        string = my_favorite_movies
    if delim == "":
        delim = default_delim
    delimeter = get_positions(string, delim)
    print(get_movies(string, delimeter))