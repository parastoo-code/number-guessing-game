# Number Guessing Game

A simple command-line number guessing game written in Python.

The program picks a secret number between 1 and 100, and the player has 5 attempts to guess it.

## Features

- Random secret number between 1 and 100
- Maximum of 5 attempts per game
- Shows the current attempt and the lives remaining on every turn
- Direction hint: "Enter a bigger number" or "Enter a smaller number"
- Closeness hint based on the difference from the secret number:
  - 5 or less: "You're very close!"
  - 6 to 15: "You're close, but still a bit far!"
  - more than 15: "You're very far!"
- Rank at the end of a winning game:

  | Winning attempt | Rank        |
  |-----------------|-------------|
  | 1               | Excellent   |
  | 2               | Very good   |
  | 3               | Good        |
  | 4               | Acceptable  |
  | 5               | Lucky win!  |

- If the player loses, a loss message is shown together with the secret number (no rank)
- Play again option after each game (a new random number and 5 fresh attempts)
- Input validation: letters, text, empty input, and numbers outside 1-100 are rejected
  without crashing the program and without using up an attempt

## How to run

1. Install Python 3.
2. Download `guess_game.py`.
3. Run it in a terminal:

```bash
python guess_game.py
```

## Example

```
Attempt 1 of 5
Lives remaining: 5
Please enter your guess (1-100): 50
Enter a smaller number - You're very far!

Attempt 2 of 5
Lives remaining: 4
Please enter your guess (1-100): abc
Invalid input! Please enter a whole number.
Please enter your guess (1-100): 20
Enter a bigger number - You're close, but still a bit far!
```
