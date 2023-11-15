import random


def is_valid(text):
    if text.isdigit():
        return 1 <= int(text) <= 100
    else:
        return False


num1 = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку!")
print('Попробуйте угадать задуманное компьютером число от 1 до 100 включительно.')

number = 0
while number != 'stop':
    print('Введите "stop", чтобы закончить или число от 1 до 100: ', end='')
    number = input()
    if number == 'stop':
        break
    if is_valid(number):
        print('Вы ввели не верное значение, повторите ввод!')
        continue
