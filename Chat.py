import tkinter as tk
import random

def check_guess():
    global attempts
    guess = int(guess_entry.get())
    attempts -= 1

    if guess < secret_number:
        result_label.config(text="Too low! Try a higher number.")
    elif guess > secret_number:
        result_label.config(text="Too high! Try a lower number.")
    else:
        result_label.config(text=f"Congratulations! You guessed the number {secret_number} in {max_attempts - attempts} attempts!")

    if attempts == 0 and guess != secret_number:
        result_label.config(text=f"Sorry, you've run out of attempts. The number was {secret_number}.")

    attempts_label.config(text=f"You have {attempts} attempts remaining.")

def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = max_attempts
    result_label.config(text="")
    attempts_label.config(text=f"You have {attempts} attempts remaining.")

# Create the main window
window = tk.Tk()
window.title("Number Guessing Game")

# Variables for the game
max_attempts = 10
secret_number = random.randint(1, 100)
attempts = max_attempts

# Widgets
instruction_label = tk.Label(window, text="Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
instruction_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

guess_button = tk.Button(window, text="Guess", command=check_guess)
guess_button.pack()

attempts_label = tk.Label(window, text=f"You have {attempts} attempts remaining.")
attempts_label.pack()

result_label = tk.Label(window, text="")
result_label.pack()

start_button = tk.Button(window, text="Start New Game", command=start_game)
start_button.pack()

# Start the GUI event loop
window.mainloop()
