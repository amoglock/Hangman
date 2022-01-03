# Write your code here
import random

words_list = ['python', 'java', 'kotlin', 'javascript']
start_game = 'Type "play" to play the game, "exit" to quit: '
win_game = '''You guessed the word!
You survived!'''
end_game = 'You lost!'


def menu():
    while True:
        choice = input(start_game)
        if choice == 'play':
            hangman()
        elif choice != 'exit':
            continue
        break


def hangman():
    guessing = random.choice(words_list)
    hint = '-' * len(guessing)
    input_letters_set = set()
    tries = 8
    answer_set = set(guessing)
    hint_list = list(hint)
    while tries > 0:
        print()
        if '-' in hint_list:
            print(''.join(hint_list))
            letter = input('Input a letter: ')
            if len(letter) == 1:
                if not letter.islower():
                    print('Please enter a lowercase English letter')
                    continue
            else:
                print('You should input a single letter')
                continue
            if letter in input_letters_set:
                print("You've already guessed this letter")
                continue
            elif letter in answer_set:
                for i in range(len(guessing)):
                    if letter == guessing[i]:
                        hint_list[i] = letter
                        input_letters_set.add(letter)
                continue
            else:
                print("That letter doesn't appear in the word")
                tries -= 1
                input_letters_set.add(letter)
                continue
        break
    if tries > 0:
        print(guessing)
        print(win_game)
        print()
        return menu()
    print(end_game)
    print()
    return menu()


print('H A N G M A N')
menu()