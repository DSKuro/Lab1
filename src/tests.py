from multiprocessing.context import assert_spawning

import pytest
from distance import calculate_distance
from circle import get_s, in_circle
from favorite_movies import get_movies
from my_family import get_family_information
from src.circle import get_s
from zoo import extend_zoo
from songs_list import get_sum_list, get_sum_dict
from secret import decrypt
from garden import get_sets
from shopping import get_sweets_with_prices
from store import calculate_costs

def test_distance():
    dist = calculate_distance({
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
    })
    assert dist['Moscow']['Moscow'] == 0.0
    assert dist['London']['London'] == 0.0
    assert dist['Moscow']['London'] == 145.60219778561037

def test_circle():
    radius = 42
    point = (3, 4)
    s = get_s(radius)
    point = in_circle(radius, point)
    assert s == 5541.7695
    assert point == 'True'

def test_movies():
    movies = get_movies('Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее', [10, 25, 33, 40])
    assert movies[0] == 'Терминатор'
    assert movies[1] == 'Назад в будущее'
    assert movies[2] == 'Пятый элемент'
    assert movies[3] == 'Пятый элемент'

def test_family():
    father_height, total_sum = get_family_information([['father', 180], ['mother', 160]])
    assert father_height == 180
    assert total_sum == 340

def test_zoo():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']
    extend_zoo(zoo, birds)
    assert zoo == ['lion', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']

def test_songs():
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

    assert get_sum_list(violator_songs_list, songs_to_sum_list) == 14.93
    assert round(get_sum_dict(violator_songs_dict, songs_to_sum_dict), 2) == 13.49

def test_secret():
    secret_message = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    s = decrypt(secret_message)
    assert s == 'в бане веник дороже денег'

def test_garden():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)
    garden_s, meadow_s = get_sets(garden, meadow)
    assert garden_s == {'подсолнух', 'одуванчик', 'роза', 'ромашка', 'гладиолус'}
    assert meadow_s == {'ромашка', 'одуванчик', 'клевер', 'мак'}

def test_shopping():
    default_shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
    }
    sweets = get_sweets_with_prices(default_shops)
    assert sweets == {'карамель': [{'price': 41.99, 'shop': 'магнит'},
              {'price': 45.99, 'shop': 'ашан'}],
                 'конфеты': [{'price': 30.99, 'shop': 'магнит'},
             {'price': 32.99, 'shop': 'пятерочка'}],
                'печенье': [{'price': 9.99, 'shop': 'пятерочка'},
             {'price': 10.99, 'shop': 'ашан'}],
                'пирожное': [{'price': 59.99, 'shop': 'пятерочка'},
              {'price': 62.99, 'shop': 'магнит'}]}

def test_store():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }
    costs = calculate_costs(goods, store)
    assert costs == {'Диван': (3, 3550),
                     'Лампа': (27, 1134),
                     'Стол': (54, 27860),
                     'Стул': (105, 10311)}
