import random

words = ["python", "computer", "program", "science", "keyboard"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")

while wrong_guesses < max_attempts:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses left:", max_attempts - wrong_guesses)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won!")
        print("The word was:", word)
        break

else:
    print("\nGame over! You lost.")
    print("The word was:", word)