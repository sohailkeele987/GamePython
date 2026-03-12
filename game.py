import random

play = "yes"

while play == "yes":

    number = random.randint(1, 10)
    guess = None
    attempts = 0

    print("\nGuess the Number Game")

    while guess != number:
        guess = int(input("Enter a number between 1 and 10: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You win in", attempts, "attempts!")

    play = input("Play again? (yes/no): ")
