# Задача 12: Петя задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

from random import randint

def get_two_numbers():
    return randint(1, 1000), randint(1, 1000)


def give_a_hint(list):
     print(f'Подсказка: {list[0]} {list[1]}\nЗагаданные числа: {list[0] + list[1]} {list[0] * list[1]}')


give_a_hint(get_two_numbers())
