#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код

# выведите на консоль все виды цветов
# TODO здесь ваш код

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код

def print_garden():
    garden_set = set(garden)
    meadow_set = set(meadow)
    all_set = garden_set | meadow_set
    print(garden_set)
    print(meadow_set)
    print(all_set)
    print(garden_set & meadow_set)
    print(garden_set - meadow_set)
    print(meadow_set - garden_set)
    return (garden_set, all_set, meadow_set - garden_set)
