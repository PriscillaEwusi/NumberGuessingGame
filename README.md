About the Project

The computer picks a secret number and you try to guess it before you run out of attempts. After each guess you are told whether you were too high or too low. The game has a menu, three difficulty levels, and a stats screen.

Features:
Loop-based main menu that repeats until you choose Exit
Three difficulty levels (Easy, Medium, Hard)
"Too high / too low" hints after every guess
Stats tracking: games played, games won, and best score
Graceful handling of invalid input (letters, empty input, out-of-range numbers)
Code organized into functions and commented step by step

Difficulty Levels:
Level	Number Range	Attempts
Easy	1 - 10	5
Medium	1 - 50	7
Hard	1 - 100	7

Requirements:
Python 3.8 or newer (no extra libraries needed)

Example
===== NUMBER GUESSING GAME =====
1. Play game
2. View stats
3. How to play
4. Exit
Choose an option (1-4): 1

Choose a difficulty:
1. Easy (1-10, 5 attempts)
2. Medium (1-50, 7 attempts)
3. Hard (1-100, 7 attempts)
Enter 1, 2 or 3: 2

I'm thinking of a number between 1 and 50.
You have 7 attempts. Good luck!

Attempts left: 7. Your guess: 25
Too low. Try a higher number.

Python Concepts Used:
Functions
while loops and break
if / elif / else
Dictionaries
try / except for input validation
The random module
