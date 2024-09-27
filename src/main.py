from distance import print_distance
from circle import print_circle
from operations import print_operation
from favorite_movies import print_movies
from my_family import print_family
from zoo import main_zoo
from songs_list import print_songs
from secret import print_secret
from garden import print_garden
from shopping import print_shopping
from store import print_store

if __name__ == "__main__":
    user_input = 0
    while True:
        print("Введите номер задачи:")
        print("1. Дистанции")
        print("2. Круг")
        print("3. Операции")
        print("4. Любимые мультфильмы")
        print("5. Семья")
        print("6. Зоопарка")
        print("7. Список песен")
        print("8. Секрет")
        print("9. Сады")
        print("10. Шоппинг")
        print("11. Магазин")
        print("12. Выход")
        try:
            user_input = int(input())
        except ValueError:
            print("Введено не число!")
            continue
        match user_input:
            case 1:
                print_distance()
            case 2:
                print_circle()
            case 3:
                print_operation()
            case 4:
                print_movies()
            case 5:
                print_family()
            case 6:
                main_zoo()
            case 7:
                print_songs()
            case 8:
                print_secret()
            case 9:
                print_garden()
            case 10:
                print_shopping()
            case 11:
                print_store()
            case 12:
                print("Выход...")
                break
            case _:
                print("Число не соответствует задаче!")
