import tkinter as tk
from tkinter import messagebox
import random

# Game Logic for Bulls and Cows
class BullsAndCows:
    def __init__(self):
        # Generate a secret 4-digit number
        self.secret_number = self.generate_secret_number()

    def generate_secret_number(self):
        return ''.join(random.sample('0123456789', 4))

    def get_feedback(self, guess):
        bulls = sum(1 for i in range(4) if guess[i] == self.secret_number[i])
        cows = sum(1 for i in range(4) if guess[i] in self.secret_number and guess[i] != self.secret_number[i])
        return bulls, cows

    def is_correct_guess(self, guess):
        return guess == self.secret_number

# GUI for Bulls and Cows
class BullsAndCowsGUI:
    def __init__(self, root):
        self.game = BullsAndCows()

        self.root = root
        self.root.title("Bulls and Cows Game")

        # Setup the layout
        self.setup_ui()

    def setup_ui(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Welcome to Bulls and Cows", font=("Arial", 14))
        self.title_label.pack(pady=10)

        # Guess Entry field
        self.guess_label = tk.Label(self.root, text="Enter your 4-digit guess:")
        self.guess_label.pack(pady=5)

        self.guess_entry = tk.Entry(self.root, width=10, font=("Arial", 14))
        self.guess_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack(pady=10)

        # Feedback Label
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

    def submit_guess(self):
        guess = self.guess_entry.get().strip()

        if len(guess) != 4 or not guess.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a 4-digit number.")
            return

        bulls, cows = self.game.get_feedback(guess)
        self.feedback_label.config(text=f"Bulls: {bulls}, Cows: {cows}")

        if self.game.is_correct_guess(guess):
            messagebox.showinfo("Congratulations!", "You guessed the secret number!")
            self.reset_game()

    def reset_game(self):
        self.game = BullsAndCows()  # Reset the game logic
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.reset_button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.NORMAL)

    def start_game(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = BullsAndCowsGUI(root)
    game.start_game()
