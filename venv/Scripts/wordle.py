import random
"""
Wordle is a word guessing game. A random target word is generated and the player
must guess the 5 letter word. If the player guess the correct letter and position,
the game feedback mechanism will return an X. If the player guess the correct letter
but incorrect position, the game return an O. If neither is true, the game returns -
"""


def get_word_list():

    result = []
    with open("C:/Users/Steve/PycharmProjects/interview/venv/Scripts/possible_words.txt") as fp:
        result.extend(word.strip() for word in fp.readlines())
    return result


def wordle():
    target = random.choice(get_word_list())
    while True:
        user_input = input("Enter your guess: ")
        user_input.strip()
        user_input.lower()

        if user_input == target:
            print("Correct! The program will now exit")
            break

        else:
            print(target)
            print(mech(target,user_input))
            print("Try Again")

    return 0




def mech(target,guess):
    result = []
    for word in guess:
        if word in target:
            if guess.index(word) == target.index(word): #If the index of the guess is the same as target
                result.extend("X")
                continue
            result.extend("O")
        else:
            result.extend("-")
    return result


print(wordle())