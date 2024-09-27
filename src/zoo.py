def print_zoo(zoo : list) -> None:
    print(zoo)

def insert_in_zoo(zoo : list) -> None:
    animal = input("Введите имя животного: ")
    position = int(input("Введите позицию: "))

    if position < 0 or position > len(zoo):
        print("Недопустимая позиция")
        return

    zoo.insert(position, animal)

def remove_from_zoo(zoo : list) -> None:
    animal = input("Введите имя убираемого животного: ")
    if animal in zoo:
        zoo.remove(animal)
    else:
        print("Такого животного нет в зоопарке")

def append_to_birds(birds : list) -> None:
    bird = input("Введите птицу: ")
    birds.append(bird)

def remove_from_birds(birds: list) -> None:
    bird = input("Введите птицу, которую хотим убрать: ")
    if bird in birds:
        birds.remove(bird)
    else:
        print("Такой птицы нет")

def extend_zoo(zoo : list, birds : list) -> None:
    zoo.extend(birds)

def get_position(zoo : list) -> int:
    animal = input("Введите имя животного, которого хотите найти: ")
    return zoo.index(animal)

def main_zoo() -> None:
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']


    while True:
        print("Введите номер задачи:")
        print("1. Показать животных")
        print("2. Показать птиц")
        print("3. Вставить животного")
        print("4. Добавить птицу")
        print("5. Убрать животного")
        print("6. Убрать птицу")
        print("7. Дополнить животных птицами")
        print("8. Найти животного")
        print("9. Выход")
        try:
            user_input = int(input())
        except ValueError:
            print("Введено не число!")
            continue

        match user_input:
            case 1:
                print_zoo(zoo)
            case 2:
                print_zoo(birds)

            case 3:
                insert_in_zoo(zoo)
            case 4:
                append_to_birds(birds)
            case 5:
                remove_from_zoo(zoo)
            case 6:
                remove_from_birds(birds)
            case 7:
                extend_zoo(zoo, birds)
            case 8:
                print(get_position(zoo))
            case 9:
                print("Выходим...")
                break
            case _:
                print("Такого номера нет!")

