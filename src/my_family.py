#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = list()

# список списков приблизителного роста членов вашей семьи
#my_family_height = [
    # ['имя', рост],
#    [],
#]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

my_family.append('father')
my_family.append('mother')
my_family.append('sister')
my_family.append('me')

my_family_height = [ ['father', 190],
                ['mother', 170],
                ['sister', 178],
                ['me', 180]
            ]

def print_family():
    print(my_family)
    print('Рост отца - ' + str(my_family_height[0][1]) + ' см')
    sum_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
    print('Общий рост семьи - ' +
        str(sum_height)
           + ' см')

    return (my_family, my_family_height[0][1], sum_height)

