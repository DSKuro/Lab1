def user_input(string : str) -> tuple:
    flowers = input(string)
    if flowers == "":
        return ()
    return tuple(flower.strip() for flower in flowers.split(','))

def get_sets(garden : tuple, meadow : tuple) -> tuple:
    garden_set = set(garden)
    meadow_set = set(meadow)
    return garden_set, meadow_set

def print_flowers_info(garden_set : set, meadow_set : set) -> None:
    print(f'Цветы, которые растут только в саду: {garden_set}')
    print(f'Цветы, которые растут только на лугу: {meadow_set}')
    print(f'Цветы, которые растут или в саду, или на лугу: {garden_set | meadow_set}')
    print(f'Цветы, которые растут и в саду, и на лугу: {garden_set &  meadow_set}')
    print(f'Цветы, которые растут в саду, но не на лугу: {garden_set - meadow_set}')
    print(f'Цветы, которые не растут в саду, но на лугу: {meadow_set - garden_set}')


def print_garden():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)

    garden_inp = user_input("Введите цветы в саду: ")
    print(garden_inp)
    if garden_inp == ():
        garden_inp = garden
    meadow_inp = user_input("Введите цветы на лужайке: ")
    if meadow_inp == ():
        meadow_inp = meadow

    garden_set, meadow_set = get_sets(garden_inp, meadow_inp)
    print_flowers_info(garden_set, meadow_set)
