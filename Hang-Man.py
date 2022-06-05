import random
import time

# Classes #

mistakes = 0


class Hangman:
    def __int__(self, mistake):
        self.mistake = mistake

    def mistake(self, mistake):
        if mistake == 1:
            print(
                ' | \n'
                '/ \\'
            )
        elif mistake == 2:
            print(
                ' | \n'
                ' | \n'\
                ' | \n'
                ' | \n'
                '/ \\'
            )
        elif mistake == 3:
            print(
                '  _ _ _ \n'
                ' | \n'
                ' | \n'
                ' | \n'
                ' | \n'
                '/ \\'
            )
        elif mistake == 4:
            print(
                '  _ _ _ _ \n'
                ' |        |\n'
                ' | \n'
                ' | \n'
                ' | \n'
                '/ \\'
            )
        elif mistake == 5:
            print(
                '  _ _ _ _ \n'
                ' |        |\n'
                ' |       _0_\n'
                ' | \n'
                ' | \n'
                '/ \\'
            )
        elif mistake == 6:
            print(
                '  _ _ _ _ \n'
                ' |        |\n'
                ' |       _0_\n'
                ' |        |\n'
                ' | \n'
                '/ \\'
            )
        elif mistake == 7:
            print(
                '  _ _ _ _ \n'
                ' |        |\n'
                ' |       _0_\n'
                ' |        |\n'
                ' |       / \\\n'
                '/ \\'
            )


# End of Classes #

# Global Variables #

global word
word = ''
global guessWord
guessWord = ''
global answer
answer = ''

hangman = Hangman()

# Start of Functions #


def checker(hiddenword, word):
    if '*' in hiddenword:
        return True


def list_to_string(hiddenword):
    str1 = ''
    for item in hiddenword:
        str1 = str1 + item

    print(str1)


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


def answer_check(inputted_answer, hideWord, word):
    hideWord = list(hideWord)
    word = list(word)
    if inputted_answer in word:
        for i in range(len(word)):
            char = word[i]
            if char == inputted_answer:
                hideWord[i] = inputted_answer
        return hideWord
    else:
        return


def gameChoice(hideWord, word):

    global mistakes
    while True:

        answer = input('Input your guess (or 1 letter of your guess): ')

        if len(answer) <= 0:
            print('Please input a valid (1) letter or your guess word.')
            continue
        elif len(answer) > len(word):
            print('Please input a valid (1) letter or your guess word.')
            continue
        elif len(answer) == len(word):
            if answer == word:
                print()
                print('\t\t********')
                print("Congrats! You win!")
                print('The word is: ', end='')
                list_to_string(word)
                print('\t\t********')
                exit()
            else:
                print('Wrong. Try harder!')
            continue
        elif len(answer) == 1 and answer in word:
            x = answer_check(answer, hideWord, word)
            print("".join(x))
            hideWord = x[:]
        elif len(answer) == 1 and answer is not word:
            mistakes = mistakes + 1
            if mistakes > 0:
                for i in range(7):
                    if i == mistakes:
                        print()
                        print(f'Current word have {len(hideWord)} letters.')
                        list_to_string(word)
                        print(f'Category: {choice}')
                        hangman.mistake(i)
                        break
                    elif i == 6:
                        print()
                        print(f'Current word have {len(hideWord)} letters.')
                        list_to_string(word)
                        print(f'Category: {choice}')
                        hangman.mistake(7)
                        print()
                        print('************')
                        print("Game Over!")
                        print('The word is: ', end='')
                        list_to_string(word)
                        print('************')
                        exit()
        elif len(answer) > 1:
            print('Please input a valid (1) letter or your guess word.')
            continue
        else:
            print('Try again!')
            continue

        if '*' in hideWord:
            continue
        else:
            print()
            print('\t\t********')
            print("Congrats! You win!")
            print('The word is: ', end='')
            list_to_string(word)
            print('\t\t********')
            time.sleep(1)
            exit()

# End of Functions #

# Lists of Words #

celebList = [
    'johnny depp',
    'denzel washington',
    'russell crowe',
    'brad pitt',
    'angelina jolie',
    'tom cruise',
    'arnold schwarzenegger',
    'sylvester stallone',
    'kate winslet',
    'christian bale',
    'morgan freeman',
    'hugh jackman',
    'bruce willis',
    'will smith',
    'george clooney',
    'scarlett johansson',
    'tom hardy',
    'robert downey jr',
    'samuel l jackson',
    'sandra bullock',
    'megan fox'
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
time.sleep(1)
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

    if (choice == 'a') or (choice == 'A'):  # ### Animals # #
        choice = 'Animals'
        word = random.choice(animalList)
        hideWord = hider(word)
        print('Your word is ', end='')
        print(hideWord)
        #print('for checking: ', word)

        gameChoice(hideWord, word)

    elif (choice == 'b') or (choice == 'B'):  # ### Food # #
        choice = 'Food'
        word = random.choice(foodList)
        hideWord = hider(word)
        print('Your word is ', end='')
        print(hideWord)
        #print('for checking: ', word)

        gameChoice(hideWord, word)

    elif (choice == 'c') or (choice == 'C'):  # ### Place # #
        choice = 'Place'
        word = random.choice(placeList)
        hideWord = hider(word)
        print('Your word is ', end='')
        print(hideWord)
        #print('for checking: ', word)

        gameChoice(hideWord, word)

    elif (choice == 'd') or (choice == 'D'):  # ### Celebrity # #
        choice = 'Celebrity'
        word = random.choice(celebList)
        hideWord = hider(word)
        print('Your word is ', end='')
        print(hideWord)
        #print('for checking: ', word)

        gameChoice(hideWord, word)

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
