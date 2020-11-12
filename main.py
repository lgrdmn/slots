import random as r
import json

values_dict = {
    'cherry': 'icon_1.jpg',
    'lemon': 'icon_2.jpg',
    'orange': 'icon_3.jpg',
    'plum': 'icon_4.jpg',
    'watermelon': 'icon_5.jpg',
    'banana': 'icon_6.jpg',
    'red7': 'icon_7.jpg',
    'bar': 'icon_8.jpg',
    'bigwin': 'icon_9.jpg'
}

bonus_values = {
    'cherry': 2,
    'lemon': 4,
    'orange': 8,
    'plum': 15,
    'watermelon': 30,
    'banana': 50,
    'red7': 150,
    'bar': 200,
    'bigwin': 500
}


def values_generator():
    """ Генератор значений слот-машины """
    keys = list(values_dict.keys())
    return r.choice(keys), r.choice(keys), r.choice(keys)


def bonus(first_value, second_value, third_value):
    """ Определение размера умножения бонуса """
    size = 0
    if first_value == second_value == third_value:
        size = bonus_values[second_value]
    return size


def get_info():
    with open("info.json", "r") as file:
        info = json.load(file)
    return info


def write_info(info):
    with open("info.json", "w") as file:
        json.dump(info, file)


def value_to_url(first_value, second_value, third_value):
    """ Получение url картинок в зависимости от значений """
    return values_dict[first_value], values_dict[second_value], values_dict[third_value]


def game(bet_size, bonus_size):
    win_size = bonus_size * bet_size
    return win_size


if __name__ == '__main__':


    credit = 100
    bet = 1

    while True:

        a, b, c = values_generator()
        multi = bonus(a, b, c)

        command = input('Введите S, если хотите начать игру или E, чтобы выйти: ')
        if command == 'S' or command == 's':
            game(bet, multi)
            credit = (credit - bet) + game(bet, multi)
            print(f'[{a}][{b}][{c}]')
            print(f'Выигрыш: {multi}')
            print(f'Баланс: {credit}')
        elif command == 'E' or command == 'e':
            break
        else:
            print('Вы ввели неверную команду.')

