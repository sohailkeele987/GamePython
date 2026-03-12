import random

number = random.randint(1, 10)
guess = None

print("Welcome to Guess the Number Game")

while guess != number:
    guess = int(input("Enter a number between 1 and 10: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You win!")