"""
Добро Пожаловать в Игру, Угадай число которое загадал ИИ

______________________________________________________________________________________________________________________
|||||||||||||||||||     ||          |||||      |||||     ||||||||||||     ||||||||||   ||    ||      |||||||
        ||              ||          || ||     ||  ||     ||        ||     ||      ||   ||  ||       ||     ||
        ||              ||          ||  ||   ||   ||     ||        ||       ||         ||||         ||     ||
        ||              ||          ||   || ||    ||     ||        ||         ||       |||||        |||||||||
        ||              ||          ||    ||||    ||     ||        ||    ||     ||     ||   ||      ||     ||
        ||              ||          ||            ||     ||||||||||||    |||||||||     ||    ||     ||     ||
_______________________________________________________________________________________________________________________
"""

from random import randint as r


computer = r(1, 100)
your_count = 0
while True:
    your_input = int(input('Введите число от 1 до 100 :'))
    your_count += 1
    if your_input == computer:
        print(f'Вы угадали число за {your_count} попыток')
        N = False
        Y = True
        change = input(f'Хотите продолжить игру ? " Y| N"')
        if change == True:
            continue
        elif change != True:
            print('Спасибо за игру ')
            break
    if your_input > computer:
        print('Загаданное число меньше вашего числа ')
    elif your_input < computer:
        print('Загаданное число больше вашего числа')

        

        

        

        

        

        
