# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.


from random import randint

def get_list():
    length = randint(1, 10)
    list = []
    for i in range(length):
        list.append(randint(0, 1))
    print(list)
    return list


def count_values(list):
    counter = 0
    for x in list:
        counter += x
    return counter if counter <= len(list)/2 else len(list) - counter


print(count_values(get_list()))
