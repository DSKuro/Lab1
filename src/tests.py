from multiprocessing.context import assert_spawning

import pytest
from distance import get_distances
from circle import print_answer
from operations import print_operation_answer
from favorite_movies import print_movies
from my_family import print_family
from zoo import print_zoo
from songs_list import print_songs
from secret import print_secret
from garden import print_garden
from shopping import print_shopping
from store import print_store

def test_distance():
    dist = get_distances()
    assert dist['Moscow']['Moscow'] == -1.0
    assert dist['London']['London'] == 0.0
    assert dist['Moscow']['London'] == 145.60219778561037

def test_circle():
    (s, in_c, out_c) = print_answer()
    assert s == 5541.7693
    assert in_c == 'True'
    assert out_c == 'False'

def test_operation():
    r = print_operation_answer()
    assert r == 25

def test_movies():
    (s1, s2, s3, s4) = print_movies()
    assert s1 != 'Терминато'
    assert s2 == 'Назад в будущее'
    assert s3 == 'Пятый элемент'
    assert s4 == 'Назад в будущее'

def test_family():
    (family, father_height, sum_height) = print_family()
    assert family == ['father', 'mother', 'sister', 'me']
    assert father_height == 190
    assert sum_height == 718

def test_zoo():
    (zoo, lion, lark) = print_zoo()
    assert zoo == ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
    assert lion == 0
    assert lark == 6

def test_songs():
    (sum1, sum2) = print_songs()
    assert round(sum1, 2) == 14.93
    assert round(sum2, 2) == 13.49

def test_secret():
    s = print_secret()
    assert s == 'в бане веник дороже денег'

def test_garden():
    (garden, all_set, m_s) = print_garden()
    assert garden == { 'ромашка', 'роза', 'одуванчик', 'гладиолус', 'подсолнух' }
    assert all_set == { 'мак', 'роза', 'подсолнух', 'гладиолус', 'ромашка', 'клевер', 'одуванчик' }
    assert m_s == { 'клевер', 'мак'}

def test_shopping():
    sweets = print_shopping()
    assert sweets == {
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
}

def test_store():
    (l1, l2, c1, c2) = print_store()
    assert l1 == 27
    assert l2 == 1134
    assert c1 == 50
    assert c2 == 5000
