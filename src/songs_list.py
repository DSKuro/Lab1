def user_input_list() -> tuple:
    songs = list()
    count = int(input("Введите количество элементов: "))
    if count <= 0:
        print("Количество элементов не может быть меньше или равно 0")
        return [], []

    for i in range(count):
        name = input("Введите имя песни: ")
        value = float(input("Введите продолжительность песни: "))
        if value <= 0.0:
            return [], []
        songs.append([name, value])

    sum_str = input("Введите песни, которые хотите посчитать: ")
    return songs, sum_str.split()

def user_input_dict() -> tuple:
    songs = {}
    count = int(input("Введите количество элементов: "))
    if count <= 0:
        print("Количество элементов не может быть меньше или равно 0")
        return {}, []

    for i in range(count):
        name = input("Введите имя песни: ")
        value = float(input("Введите продолжительность песни: "))
        if value <= 0.0:
            return {}, []
        songs[name] = value

    sum_str = input("Введите песни, которые хотите посчитать: ")
    return songs, sum_str.split()

def get_sum_list(songs: list, total_sum : list) -> float:
    return sum(round(song[1], 2) for song in songs if song[0] in total_sum)

def get_sum_dict(songs: dict, total_sum : list) -> float:
    return sum(round(songs[song], 2) for song in total_sum)


def print_songs():
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]

    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }

    songs_to_sum_list = ['Halo', 'Enjoy the Silence', 'Clean']
    songs_to_sum_dict = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']

    songs, total_sum = user_input_list()
    if songs == [] or total_sum == []:
        songs = violator_songs_list
        total_sum = songs_to_sum_list

    print(get_sum_list(songs, total_sum))

    songs_dict, total_sum_dict = user_input_dict()
    if songs_dict == {} or total_sum_dict == []:
        songs_dict = violator_songs_dict
        total_sum_dict = songs_to_sum_dict

    print(f'{get_sum_dict(songs_dict, total_sum_dict):.2f}')
