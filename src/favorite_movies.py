#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
def print_movies():
    print(my_favorite_movies[:10])
    print(my_favorite_movies[42:])
    print(my_favorite_movies[12:25])
    print(my_favorite_movies[-15:])
    return (my_favorite_movies[:10], my_favorite_movies[42:],
            my_favorite_movies[12:25], my_favorite_movies[-15:])
