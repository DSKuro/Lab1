def get_goods_input() -> dict:
    goods = {}
    while True:
        item_name = input("Введите название товара: ")
        if item_name == '':
            break
        item_code = input("Введите код товара: ")
        goods[item_name] = item_code
    return goods

def get_store_input() -> dict:
    store = {}
    while True:
        code = input("Введите код товара: ")
        if code == '':
            break
        quantity = int(input("Введите количество: "))
        price = float(input("Введите цену: "))
        if code not in store:
            store[code] = []
        store[code].append({'quantity': quantity, 'price': price})
    return store

def calculate_costs(goods, store):
    results = {}
    for item, code in goods.items():
        if code in store:
            total_quantity = sum(entry['quantity'] for entry in store[code])
            total_cost = sum(entry['quantity'] * entry['price'] for entry in store[code])
            results[item] = (total_quantity, total_cost)
    return results

def print_store():
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

    print("Введите товары: ")
    user_goods = get_goods_input()
    print("Товары на складе: ")
    user_store = get_store_input()

    if not user_goods:
        user_goods = goods
    if not user_store:
        user_store = store

    costs = calculate_costs(user_goods, user_store)
    for item, (quantity, cost) in costs.items():
        print(f'{item} - {quantity} шт, стоимость {cost} руб')