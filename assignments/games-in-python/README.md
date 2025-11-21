# 📘 Assignment: Hangman Game Challenge

## 🎯 Objetivo

Build the classic word-guessing game using Python strings, loops, and user input. Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

**Skills practiced:** String manipulation, loops, conditionals, random selection

## 📝 Tarefas

### 🛠️ Random Word Selection

#### Description
Randomly select a word from a predefined list for the player to guess.

#### Requirements
Completed program should:

- Include a predefined list of words.
- Randomly select one word from the list at the start of the game.
- Ensure the same word is not selected repeatedly in a single session.

### 🛠️ Letter Guessing and Progress Display

#### Description
Accept letter guesses from the player and display the current progress of the word.

#### Requirements
Completed program should:

- Accept user input for letter guesses.
- Display the word's progress using underscores for unguessed letters (e.g., `_ _ _`).
- Update the display as correct letters are guessed.
- Ignore case sensitivity in guesses.

### 🛠️ Incorrect Guess Tracking

#### Description
Track the number of incorrect guesses remaining and end the game appropriately.

#### Requirements
Completed program should:

- Start with a predefined number of attempts (e.g., 6).
- Decrease the remaining attempts for each incorrect guess.
- End the game when the word is guessed or attempts are exhausted.
- Display appropriate win/lose messages at the end of the game.
