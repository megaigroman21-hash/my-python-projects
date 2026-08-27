digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert_from_10(num_in_10, q):
    if num_in_10 == 0:
        return '0'
    
    result = ''
    while num_in_10 != 0:
        index = num_in_10 % q
        result += digits[index]
        num_in_10 = num_in_10 // q
    return result[::-1]


def correct_num(base_p):
    while True:
        t = input('Введите ваше число: ').upper()
        correct = True
        allowed_digits = digits[:base_p]
        for char in t:
            if char not in allowed_digits:
                correct = False
                break

        if not correct or t == '':
            print('Некорректный ввод, повторите попытку =(')
        else:
            return t


def correct_p_q(prompt, error_message):
    while True:
        t = input(prompt)
        if t.isdigit() and 2 <= int(t) <= 36:
            return int(t)
        else:
            print(error_message)


print('Здравствуйте! Это программа для перевода чисел в разные системы счисления. Приятного использования 🐍✨')
p = correct_p_q('Введите начальную систему счисления вашего числа: ', 'Некорректный ввод, повторите попытку =(')
q = correct_p_q('Введите, в какую систему счисления надо перевести ваше число: ', 'Некорректный ввод, повторите попытку =(')

num = correct_num(p)

num_in_10 = int(num, p)

if q == 10:
    print(f'Результат: {num_in_10}')
else:
    print(f'Результат: {convert_from_10(num_in_10, q)}')

print('Спасибо, что воспользовались моей программой. До свидания 🔚')
