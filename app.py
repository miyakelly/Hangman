import random
from hangman_viz import lives_visual_dict as viz
# import string
from words import words_list


def get_valid_word(x):
    word = random.choice(x)
    while '-' in word or ' ' in word or len(word) < 4:
        word = random.choice(x)
    return word.lower()


def hangman():
    word = get_valid_word(words_list)  # select a word
    word_list = list(word)  # return the word in a list format
    guessed_letter = []  # initial stage of the guessed letter list object
    letter_placeholder = "_" * len(word)
    init_letter_list = list(letter_placeholder)  # turn letter_placeholder into a list, so the outcome is ['_', ' ', '_', ' ', blabla]
    updated_guessed_letter_list = list(letter_placeholder)  # new list

    print(word_list)
    guesses = 0

    print(f"""
    Let's play
    {viz[guesses]}
    {letter_placeholder} - this is the placeholder
    {word} - this is the word
    """)

    while guesses < 6:
        guess = str(input('Guess a letter: ')).lower()
        if len(guess) > 1:
            print('One letter at a time.')
            print(guesses)
        elif len(guess) < 1 or guess == "":
            print('Enter a letter.')
            print(guesses)
        elif guess in guessed_letter:
            print(f"""
    You have guessed this letter.
    The letters you have guessed are: {''.join(guessed_letter)}
            """)
            print(guesses)
        else:
            guessed_letter.append(guess)
            i = 0  # this i is different from guesses. It's for the location of the guessed letter
            while i < len(word):
                if guess == word[i]:
                    updated_guessed_letter_list[i] = word_list[i]
                i += 1
            print(f'{updated_guessed_letter_list} - updated_list')
            print(f'{init_letter_list} - init_letter_list')

            if updated_guessed_letter_list == init_letter_list:
                print('The guessed letter is not in the word')
                guesses += 1
                print(viz[guesses])
    #             if guesses < 6:
    #                 print('Guess again.')
    #                 print(" ".join(updated_guessed_letter_list))
            elif word_list != init_letter_list:
                init_letter_list = updated_guessed_letter_list[:]
                print(' '.join(init_letter_list))
                if word_list == init_letter_list:
                    print('You win!')


hangman()