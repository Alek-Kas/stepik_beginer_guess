import random


def is_valid(text):
    if text.isdigit():
        return 1 <= int(text) <= 100
    else:
        return False


rand_num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку!")
print('Попробуйте угадать задуманное компьютером число от 1 до 100 включительно.')
number_of_tries = 0
number = 0
#while number != 'stop' and number != rand_num:
while number != 'stop':
    print('Введите "stop", чтобы закончить или число от 1 до 100: ', end='')
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
        print('Если хотите закончить игру введите слово "stop", любой другой ввод перезапустит игру:', end='')
        number = input()


print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
