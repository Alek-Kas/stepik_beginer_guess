import random


def is_valid(text):
    if text.isdigit():
        return 1 <= int(text) <= 100
    else:
        return False


def change_max_num():
    print('Если хотите изменить максимальное число для загадывания введите "y": ', end='')
    ch_max_num = input()
    if ch_max_num == 'Y' or ch_max_num == 'y':
        print('Введите целое число больше 1: ', end='')
        num = input()
        while not num.isdigit() or int(num) < 1:
            print('Введите целое число больше 1: ', end='')
            num = input()
        return int(num)
    else:
        return max_num


def default_values():
    return 0, 0, change_max_num()


max_num = 100
print("Добро пожаловать в числовую угадайку!")
print(f'Попробуйте угадать задуманное компьютером число от 1 до {max_num} включительно.')
number_of_tries, number, max_num = default_values()
rand_num = random.randint(1, max_num)
while number != 'stop':
    # print(f'Задуманное число равно = {rand_num}, максимальное = {max_num}')  # для тестов
    print(f'Введите "stop", чтобы закончить или число от 1 до {max_num}: ', end='')
    number = input()
    number_of_tries += 1
    if number == 'stop':
        break
    if is_valid(number):
        number = int(number)
    else:
        print('Вы ввели не верное значение, повторите ввод!')
        continue
    if number < rand_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif number > rand_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print()
        print('Вы угадали, поздравляем!')
        print('*' * number_of_tries)
        print(f'Было сделано {number_of_tries} попыток')
        print('-' * 20)
        print('Если хотите закончить игру введите слово "stop", любой другой ввод перезапустит игру: ', end='')
        number = input()
        if number != 'stop':
            number_of_tries, number, max_num = default_values()
            rand_num = random.randint(1, max_num)

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
