from random import * 

word_list = [
    "питон", "программа", "компьютер", "алгоритм", "функция",
    "скрипт", "данные", "разработчик", "интерфейс", "процессор",
    "монитор", "клавиатура", "мышка", "ноутбук", "сервер",
    "память", "диск", "видеокарта", "матрица", "микрофон",
    "кодинг", "отладка", "компилятор", "переменная", "массив",
    "объект", "класс", "модуль", "библиотека", "фреймворк",
    "терминал", "консоль", "репозиторий", "индекс", "запрос",
    "байт", "бит", "трафик", "интернет", "браузер",
    "хостинг", "домен", "провайдер", "протокол", "роутер",
    "хакер", "безопасность", "пароль", "логин", "аккаунт"
]


def get_word(random_word):
    result = choice(random_word).upper()
    return result


def display_hangman(tries):

    stages = [
        # Финальное состояние (tries = 0): голова, торс, обе руки, обе ноги
        """
           --------

           |      |
           |      O

           |     /|\\
           |     / \\
           -
        """,
        # 1 попытка (tries = 1): голова, торс, обе руки, одна нога
        """
           --------

           |      |
           |      O

           |     /|\\
           |     /
           -
        """,
        # 2 попытки (tries = 2): голова, торс, обе руки
        """
           --------

           |      |
           |      O

           |     /|\\
           |
           -
        """,
        # 3 попытки (tries = 3): голова, торс и одна рука
        """
           --------

           |      |
           |      O

           |     /|
           |
           -
        """,
        # 4 попытки (tries = 4): голова и торс
        """
           --------

           |      |
           |      O

           |      |
           |
           -
        """,
        # 5 попыток (tries = 5): только голова
        """
           --------

           |      |
           |      O
           |
           -
        """,
        # Начальное состояние (tries = 6): пустая виселица
        """
           --------

           |      |
           |
           |
           -
        """
    ]
    return stages[tries]

def play(word):
    word = word.upper()
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6   
    print('Давай играть в угадайку слов!')      
    print(display_hangman(tries))               
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input('Введи букву или слово целиком: ').upper().strip()

        if not guess.isalpha():
            print('Некорректный ввод. Повтори попытку.')
            continue
        if len(guess) == 1:
            if guess in guessed_letters:
                print(f'Ты уже называл букву {guess}. Твоя попытка не засчитывается.')
            elif guess not in word:
                print(f'Буквы {guess} нет в слове.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f'Отлично! Буква {guess} есть в слове.')
                guessed_letters.append(guess)

                word_as_list = list(word_completion)
                for index in range(len(word)):
                    if word[index] == guess:
                        word_as_list[index] = guess

                word_completion = ''.join(word_as_list)

                if '_' not in word_completion:
                    guessed = True

        elif len(guess) == len(word):
            if guess in guessed_words:
                print(f'Ты уже называл слово {guess}. Твоя попытка не засчитывается.')
            elif guess != word:
                print(f'Ты не угадал. Слово {guess} не подходит.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print(f'Длина твоего слова не совпадает с количеством букв в загаданногом слове. Количество букв в загаданном слове: ({len(word)})')
            continue

        print(display_hangman(tries))
        print(word_completion)
        print(f'Осталось попыток: {tries}')
        print()

    if guessed:
        print(f'Ты угадал, молодец!')
    else:
        print(f'Не смог ты слово отгадать: {word} =(')
 
word = get_word(word_list)

play(word)
