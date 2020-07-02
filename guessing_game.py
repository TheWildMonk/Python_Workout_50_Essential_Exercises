# 1.2 Number Guessing Game

# Importing required library
import random

# Initial statements
print("Welcome to the Number Guessing Game")
print("You'll get 5 attempts to guess the right number picked by Computer between 13 - 29")
print("Let's go!!!")
print()

# Random number generation
secret_number = random.randint(13, 29)

# Attempt counter
number_trial_count = 0

# The guessing loop
while True:
    try:
        # User input
        user_input = int(input("Please enter an integer: "))

        # Conditions
        if user_input == secret_number:
            print(f"You've guessed correctly. The computer generated number was {secret_number} as well!")
            break
        elif user_input > secret_number:
            print("Your guess is too high")
        elif user_input < secret_number:
            print("Your guess is too low")

        # Attempt increment
        number_trial_count += 1
        if number_trial_count == 5:
            print(
                f"You have used all your attempts. Computer guessed '{secret_number}'. Better luck next time, ciao!!!")
            break

    except ValueError:
        print("You've entered a non-integer value, please try again!")

print()

# 1.2.3 Random Word Guessing

# Importing required library
from random_word import RandomWords

# Initial Statement
print("Welcome to the Word Guessing Game")
print("You'll get 5 attempts to predict the word")
print("Let's go!!!")

# Random word generation & giving hint to the participant

r_word = RandomWords()
secret_word = r_word.get_random_word()
first_letter = list(secret_word)
print(
    f"The length of the word is {len(secret_word)}. Starting Letter: {first_letter[0]}, Ending Letter: {first_letter[len(secret_word) - 1]}.")

# Trial counter
word_trial_count = 0

while True:

    # Exception handling
    try:
        user_word_input = str(input("Please enter a 2 - 5 letter word from the beginning of dictionary: "))

        if user_word_input == secret_word:
            print(f"You've guessed correctly. The computer generated word was {secret_word} as well")
            break
        elif len(user_word_input) == len(secret_word):
            print("You have used correct number of letters. But it's not the word, try again!")
        elif len(user_word_input) > len(secret_word):
            print("Your word contains more letter than the secret word")
        elif len(user_word_input) < len(secret_word):
            print("Your word contains less letter than the secret word")

        word_trial_count += 1
        if word_trial_count == 5:
            print(f"You've used all attempts. Computer predicted {secret_word}. Better luck next time, ciao!!!")
            break

    except ValueError:
        print("You have entered a non-string value, please try again.")