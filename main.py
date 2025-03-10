import tkinter as tk
import random
import nltk
from nltk.corpus import words

# Download the word list if not already downloaded
nltk.download("words")

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        # Get a random word from nltk corpus
        self.word_list = words.words()
        self.secret_word = random.choice(self.word_list).lower()
        self.display_word = ["_" for _ in self.secret_word]
        self.guesses_left = 5
        self.wrong_guesses = 0
        self.hint_given = False

        self.label = tk.Label(root, text="Welcome to Hangman!", font=("Arial", 16))
        self.label.pack(pady=10)

        self.word_label = tk.Label(root, text=" ".join(self.display_word), font=("Arial", 14))
        self.word_label.pack(pady=10)

        self.input_label = tk.Label(root, text="Guess a letter:", font=("Arial", 12))
        self.input_label.pack()

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess, font=("Arial", 12))
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(root, text=f"Guesses left: {self.guesses_left}", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.hint_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.hint_label.pack()

    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.result_label.config(text="Invalid input! Enter a single letter.")
            return

        if guess in self.secret_word:
            for index, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.display_word[index] = guess
        else:
            self.guesses_left -= 1
            self.wrong_guesses += 1
            self.result_label.config(text=f"Guesses left: {self.guesses_left}")

            # Provide hint after 2 wrong guesses
            if self.wrong_guesses == 2 and not self.hint_given:
                self.hint_label.config(text=f"Hint: The word starts with '{self.secret_word[0]}'")
                self.hint_given = True

        self.word_label.config(text=" ".join(self.display_word))

        if "_" not in self.display_word:
            self.result_label.config(text="You Win! 🎉")
            self.submit_button.config(state=tk.DISABLED)

        if self.guesses_left == 0:
            self.result_label.config(text=f"You Lost! The word was '{self.secret_word}'.")
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
