import random
from words import words_list
from hangman_viz import lives_visual_dict as viz


def get_word(answer):
    word = random.choice(answer)
    while ' ' in word or '-' in word or len(word) < 4:
        word = random.choice(answer)
    return word.lower()


def hangman():
    final_word = get_word(words_list)
    word_list = list(final_word)  # make final_word into a list
    user_guess = []  # capture what user has guessed
    placeholder = '_' * len(final_word)
    updated_list = list(placeholder)  # make updated list into a list to compare
    lives = 7

    print(f'''
{viz[lives]}
You have {lives} tries.
{final_word}
''')

    while lives > 0:
        guess = str(input('Guess a letter: ')).lower()
        if len(guess) > 1:
            print('One letter at a time.')
        elif len(guess) < 1 or guess == "":
            print('Enter a letter.')
        elif guess in user_guess:
            print(f"""
    You have guessed this letter.
    The letters you have guessed are: {''.join(user_guess)}
            """)
        else:
            user_guess.append(guess)  # add the guessed letter into the user_guess list
            is_guess_wrong = True
            i = 0
            while i < len(final_word):  # if out of bound error received, add -1
                if guess == word_list[i]:
                    updated_list[i] = word_list[i]
                    is_guess_wrong = False
                i += 1

            if updated_list == word_list:
                print('you won!')
                break

            elif updated_list != word_list:  # two scenarios: 1. guess wrong, 2. guess right letter but not all
                if is_guess_wrong:
                    lives -= 1
                    print(f'''
{viz[lives]}
The letter is not in the word. You now have {lives} lives.
Your guesses so far is {''.join(updated_list)}
''')
                else:
                    print(f'''
You guessed one letter right!
Your guesses so far is {''.join(updated_list)}
''')


hangman()
