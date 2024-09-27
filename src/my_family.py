def user_input() -> tuple:
    my_family = list()
    my_family_height = list()

    num = int(input("Введите количество элементов: "))

    if num <= 0:
        print("Количество не может быть меньше или равно 0")
        return 0, 0

    for _ in range(num):
        name = input("Введите члена семьи: ")
        value = int(input("Введите рост члена семьи: "))
        my_family.append(name)
        my_family_height.append([name, value])

    return my_family, my_family_height

def get_family_information(height : list) -> tuple:
    total_sum = sum(member[1] for member in height)
    father_height = height[0][1]

    return father_height, total_sum

def print_family():
    my_family, heights = user_input()
    if my_family == 0 and heights == 0:
        return
    print(my_family)
    father_height, total_sum = get_family_information(heights)
    print('Рост отца - ' + str(father_height) + ' см')
    print('Общий рост семьи - ' +
        str(total_sum)
           + ' см')

