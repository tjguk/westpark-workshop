import random

DEBUG = True

all_words = open("words.txt").read().split()
chosen_word = random.choice(all_words)
if DEBUG:
    print("The chosen word is:", chosen_word)

while True:
    guessed_word = input("Guess: ").upper()
    if guessed_word == chosen_word:
        print("You win!")
        break

    score = 0
    if guessed_word[0] == chosen_word[0]:
        score = score + 1
    if guessed_word[1] == chosen_word[1]:
        score = score + 1
    if guessed_word[2] == chosen_word[2]:
        score = score + 1
    print("You score:", score)
