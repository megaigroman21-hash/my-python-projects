def correct_user_input_direction_and_language(prompt, options, error_message):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in options:
            return user_input
        else:
            print(error_message)
    

def correct_user_input_shift(prompt, error_message):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            user_input = int(user_input)
            return user_input  
        else:
            print(error_message)

    
direction = correct_user_input_direction_and_language('Выберите нужную опцию (шифровать / дешифровать): ',
['шифровать', 'дешифровать'], 'Введены некорректные данные. Обратите внимание, можно ввести только "шифровать" или "дешифровать"')

language = correct_user_input_direction_and_language('Выберите язык с которым хотите работать (русский / английский): ',                                                    
['русский', 'английский'], 'Введены некорректные данные. Обратите внимание, программа работает только с "русский" или "английский" языками.')

shift = correct_user_input_shift('Какой шаг сдвига у вашего текста? (введите целое число): ', 'Введены некорректные данные, введите число')
text = input('Введите ваш текст: ')

EN_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
RU_ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

if language == 'русский':
    alph = RU_ALPHABET   
else:
    alph = EN_ALPHABET
    
if direction == 'дешифровать':
    shift = -shift

new_text = ''
for symbol in text:
    if symbol.lower() in alph:

        index = alph.find(symbol.lower())

        if symbol.isupper():
            new_text += alph[(index + shift) % len(alph)].upper()
        else:
            new_text += alph[(index + shift) % len(alph)]

    else:
        new_text += symbol
            
print(new_text)

