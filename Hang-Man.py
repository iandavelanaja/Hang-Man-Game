import random
import time

# Global Variables #

global word
word = ''
global guessWord
guessWord = ''
global answer
answer = ''

# Start of Functions #


def hider(word):
    global guessWord
    for char in word:
        if char == ' ':
            char = ' '
        else:
            char = '*'
        guessWord = guessWord + char
    guessWord = guessWord
    return guessWord

# End of Functions #

# Lists of Words #

celebList = [
    'johnny depp',
    'Denzel Washington',
    'Russell Crowe',
    'Brad Pitt',
    'Angelina Jolie',
    'Tom Cruise',
    'Arnold Schwarzenegger',
    'Sylvester Stallone',
    'Kate Winslet',
    'Christian Bale',
    'Morgan Freeman',
    'Hugh Jackman',
    'Bruce Willis',
    'Will Smith',
    'George Clooney',
    'Scarlett Johansson',
    'Tom Hardy',
    'Robert Downey Jr',
    'Samuel L Jackson',
    'Sandra Bullock',
    'Megan Fox'
]
foodList = [
    'salad',
    'chicken',
    'cheese',
    'apples',
    'pizza',
    'sausage',
    'bread',
    'beef',
    'steak',
    'pork',
    'oranges',
    'grapes,'
    'cassava',
    'soybeans',
    'banana',
    'meatloaf',
    'fish',
    'sushi',
    'ramen'
]
placeList = [
    'new zealand',
    'paris',
    'hawaii',
    'united states of america',
    'france',
    'germany',
    'maldives',
    'siargao',
    'barcelona',
    'venice'
]
animalList = [
    'dog',
    'cat',
    'kangaroo',
    'panda',
    'tiger',
    'orangutan',
    'gorilla',
    'giraffe',
    'lion',
    'rhinoceros',
    'hippopotamus',
    'armadillo',
    'zebra',
    'horse',
    'llama',
    'elephant'
]

# End of List of Words #

print("Welcome to Hang-Man!")
print("What\'s your name? ", end='')

name = input()

print(f'Hello {name}! Best of Luck. Let\'s go!')
print('The game is about to start...')
time.sleep(2)
print()
print('****************')
print('Let\'s play Hang-man!')

# Game Starts Here

while True:
    print('****************')
    print("Please choose a category: ")
    print("a: Animals")
    print("b: Food")
    print("c: Place")
    print("d: Celebrity")
    print("e: Quit Game")
    print('-')

    choice = input()

    chances = True

    if (choice == 'a') or (choice == 'A'):  # ### Animals # #
        word = random.choice(celebList)
        print('Your word is ', end='')
        print(hider(word))
        print(word)

        word = list(word)

        while chances:

            answer = input('Input your guess (or 1 letter of your guess): ')

            if len(answer) < 0:
                continue
            elif len(answer) > 1:
                continue
            elif len(answer) > len(word):
                continue
            elif len(answer) == len(word):
                if answer == word:
                    print('You got it right!!')
                    exit()
                else:
                    print('Wrong. Try harder!')
                continue
            elif len(answer) == 1:
                if answer in word:
                    for char in word:
                        if char in word:
                            char = char
                        elif char == ' ':
                            char = ' '
                        else:
                            char = '*'
                        word.append(char)

                    word = ''.join(word)
                    print(word)
            else:
                print('Try again!')
                continue

        # print(word)

    elif (choice == 'b') or (choice == 'B'):  # ### Food # #
        pass

    elif (choice == 'c') or (choice == 'C'):  # ### Place # #
        pass

    elif (choice == 'd') or (choice == 'D'):  # ### Celebrity # #
        pass

    elif (choice == 'e') or (choice == 'E'):  # ### Quit Game # #
        print('The game will quit in ')
        for num in range(3, 0, -1):
            print(num, '..')
            time.sleep(1)
        exit()
    else:
        print('Choice not recognized. Please choose within the given choices..')
        time.sleep(1)
        continue
    exit()
exit()
