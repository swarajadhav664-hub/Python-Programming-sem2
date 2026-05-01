# exp 10 act 2
"""
Created on Fri May  1 22:54:27 2026

@author: swaranjali jadhav
"""

# 4. Number Guessing Game
def guessing_game():
    number = random.randint(1, 100)
    guess = None

    print("Guess a number between 1 and 100")

    while guess != number:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You guessed it!")
