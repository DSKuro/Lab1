#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Расставьте знаки операций "плюс", "минус", "умножение" и скобки
# между числами "1 2 3 4 5" так, что бы получилось число "25".
#
# Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
# Порядок чисел нужно сохранить.

# Пример для чисел "1 2 3" и "9"

import itertools

def user_input() -> tuple:
    numbers = [int(x) for x in input("Введите выражение: ").split()]
    target = int(input("Введите ожидаемый результат: "))
    return numbers, target

def generate_operations(operations : list, length : int) -> list:
    return list(itertools.product(operations, repeat=length))

def generate_expressions(numbers : list, operations : list) -> list:
    if len(numbers) == 1:
        return [str(numbers[0])]

    expressions = []
    for i in range(len(numbers) - 1):
        left_numbers = numbers[:i + 1]
        right_numbers = numbers[i + 1:]

        left_expressions = generate_expressions(left_numbers, operations)
        right_expressions = generate_expressions(right_numbers, operations)

        for left in left_expressions:
            for right in right_expressions:
                for operation in operations:
                    expressions.append(f'({left} {operation} {right})')

    return expressions

def generate_all_expressions(numbers : list) -> list:
    operations = ['+', '-', '*', '/']
    expressions = []

    for ops in generate_operations(operations, len(numbers) - 1):
        exprs = generate_expressions(numbers, ops)
        expressions.extend(exprs)

    return expressions

def filter_expressions(expressions : list, target : int) -> list:
    valid_expressions = []
    for expr in expressions:
        try:
            if eval(expr) == target:
                valid_expressions.append(expr)
        except ZeroDivisionError:
            continue
    return valid_expressions

def get_operation_result(expression: list, result : int) -> list:
    all_expressions = generate_all_expressions(expression)
    valid_expressions = filter_expressions(all_expressions, result)
    return valid_expressions

def print_operation():
    expression, result = user_input()
    print(get_operation_result(expression, result))
