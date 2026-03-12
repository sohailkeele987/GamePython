import tkinter as tk
import random

number = random.randint(1, 10)

def check_guess():
    guess = int(entry.get())

    if guess < number:
        result.config(text="Too Low!")
    elif guess > number:
        result.config(text="Too High!")
    else:
        result.config(text="Correct!")

root = tk.Tk()
root.title("Guess The Number")

label = tk.Label(root, text="Guess number 1-10")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Guess", command=check_guess)
button.pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()

