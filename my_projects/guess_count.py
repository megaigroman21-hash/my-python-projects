from random import *

print('Добро пожаловать в числовую угадайку')

def is_valid(num, t):
    return num.isdigit() and 1 <= int(num) <= t
     

while True:
    
    t = int(input("Напишите правую границу генерации чисел: "))
    random_num = randint(1, t)
    count = 0
    while True:
    
        user = input(f'Введите ваше число от 1 до {t}: ') 
    
        if not is_valid(user, t):
            print(f'А может быть все-таки введем целое число от 1 до {t}? ')
            continue

        count += 1
        num = int(user)

        if num < random_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')

        elif num > random_num:
            print('Ваше число больше загаданного, попробуйте еще разок')

        elif num == random_num:
            print('Вы угадали, поздравляем!', 'Ваше количество попыток', str(count) + '.')
            break

    answer = input('Хотите сыграть еще раз? (введите "да" или любой другой текст для выхода): ')
    if answer.lower() != 'да':
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
