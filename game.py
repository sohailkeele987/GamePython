import tkinter as tk
import random

number = random.randint(1, 10)
attempts = 0

def check_guess():
    global attempts
    attempts += 1

    guess = int(entry.get())

    if guess < number:
        result.config(text="Too Low!")
    elif guess > number:
        result.config(text="Too High!")
    else:
        result.config(text=f"Correct in {attempts} attempts!")

root = tk.Tk()
root.title("Guess The Number Game")

label = tk.Label(root, text="Guess number between 1 and 10")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit Guess", command=check_guess)
button.pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()