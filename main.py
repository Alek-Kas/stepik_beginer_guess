import random


def is_valid(text):
    if text.isdigit():
        return 1 <= int(text) <= 100
    else:
        return False


num1 = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку")

number = input()
print(is_valid(number))
