import random

HANGMAN = (
'''
    +---+
    |   |
        |
        |
        |
        |
 =========
''',
'''

    +---+
    |   |
    O   |
        |
        |
        |
 =========
''',
'''

    +---+
    |   |
    O   |
    |   |
        |
        |
 =========
''',
'''

    +---+
    |   |
    O   |
   /|   |
        |
        |
 =========
''',
'''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
 =========
''',
'''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 =========
''',
'''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
''')



print('''Добро пожаловать в игру "Виселица"!
Сейчас я загадаю слово, а вы  должны будете по буквам его угадать.
За каждую ошибку будет дорисовываться человечек.
Удачи!
'''
)

def game_hangman():
    MAX_WRONG = len(HANGMAN) - 1
    WORDS = ('''СТРЕЛКА, ГРАДУСНК, ШКОЛА, БУТЫЛКА, ЩИПЦЫ, НАВОЛОЧКА, АНЕКДОТ, КАРТОЧКА, ПАВЛИН, ЗАПИСКА, ЛЕСТНИЦА, ПЕРЕУЛОК, ЗАКАТ''')
    word = random.choice(WORDS)
    so_far = '-' * len(word)
    wrong = 0
    used = []
    while wrong < MAX_WRONG and so_far != word:
        print(HANGMAN[wrong])
        print('\nУже предложенные буквы:\n', used)
        print('\nСлово сейчас выглядит так:\n', so_far)

        guess = input('\n\nВведите букву: ')
        guess = guess.upper()
        while guess in used:
            print('Вы уже предлагали букву: ', guess)
            guess = input('\n\nВведите букву: ')
            guess = guess.upper()
        used.append(guess)

        if guess in word:
            print('\nДа! Буква', guess, 'есть в слове!')
            new = ''
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new
        else:
            print('\nБуквы', guess, 'нет в слове.')
            wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print('\nЧеловечка повесили!')
    else:
        print('\nВы отгадали!')

    print('\nБыло загаданно слово', word, '.')
    game_again()


def game_again():
    game = input('Сыграем еще раз?\n (Да/Нет)')
    if game=='Да' or game=='да':
        game_hangman()
    else:
        print('Спасибо за игру!')
        exit()


game_hangman()
