import random
guesses_made = 0

name = input('Привет! Как тебя зовут?\n')
while True:
    rang = int(input('До какого числа я буду загадывать число?\n'))
    number = random.randint(1, rang)
    print('Отлично, {0},я загадал число между 1 и {1}. Сможешь угадать?'.format(name, rang))

    while guesses_made < 6:
        guess = int(input('Введи число: '))
        guesses_made += 1

        if guess < number:
            print('Твое число меньше того, что я загадал.')

        if guess > number:
            print('Твое число больше загаданного мной.')

        if guess == number:
            break

    if guess == number:
        print('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
    else:
        print('А вот и не угадал! Я загадал число {0}'.format(number))

    game = input('Сыграем еще раз, {0}?\n (Да/Нет)'.format(name))

    if game=='Да' or game=='да':
        guesses_made = 0
        True
    else:
        print('Спасибо за игру, {0}!'.format(name))
        break
