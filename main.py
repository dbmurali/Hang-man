import random
import random
import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import  stages
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
used_letters=[]
while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess not in used_letters:
        used_letters.append(guess)
        print(used_letters)

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                 display += "_"

        print("Word to guess: " + display)




        if guess not in chosen_word:
            lives -= 1
            print(f"{guess}: NOT IN THE WORD")
            if lives == 0:
                game_over = True
                print(f"THE  CORRET WORD IS: {chosen_word}")

                # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
                print(f"***********************\"YOU LOSE\"**********************")

        if "_" not in display:
            game_over = True
            print("****************************\"YOU WIN\"****************************")

        # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
        print(stages[lives])
    else:
        print("\"You've already guessed a\"")