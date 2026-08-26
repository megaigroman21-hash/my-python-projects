from random import choices

def generate_password(len_password, chars):
    password = choices(chars, k=len_password)
    print(f"{i}) {''.join(password)}")


digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
similar = 'il1Lo0O'

print('Добро пожаловать в генератор паролей!')

cnt_password = int(input("Сколько вам надо паролей? "))
while True:
    len_password = int(input('Какая длина пароля вам нужна? (минимум 14): '))
    if len_password >= 14:
        break
    print('Ошибка: длина пароля должна быть не менее 14 символов! Попробуйте еще раз.')

digits_password = input('Добавить цифры в пароль? Введите да/нет. ')
uppercase_password = input('Добавить прописные буквы в пароль? Введите да/нет. ')
lowercase_password = input('Добавить строчные буквы в пароль? Введите да/нет. ')
punctuation_password = input("Добавить символы '!#$%&*+-=?@^_'? Введите да/нет. ")
similar_password = input("Добавить неоднозначные символы 'il1Lo0O'? Введите да/нет. ")
 
chars = ''
if digits_password.lower() == 'да':
    chars += digits
if uppercase_password.lower() == 'да':
    chars += uppercase_letters
if lowercase_password.lower() == 'да':
    chars += lowercase_letters
if punctuation_password.lower() == 'да':
    chars += punctuation
if similar_password.lower() == 'да':
    chars += similar

print('Ваши пароли:')

for i in range(1, cnt_password + 1):
    generate_password(len_password, chars)
    
print()
print('До свидания, надежной защиты!')
