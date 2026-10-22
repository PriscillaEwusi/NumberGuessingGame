
import random  # lets us pick a random secret number
 
# ---------------------------------------------------------------
# STEP 1: Game settings
# Each difficulty has a range of numbers and a max number of attempts.
# ---------------------------------------------------------------
DIFFICULTIES = {
    "1": {"name": "Easy",   "max_number": 10,  "attempts": 5},
    "2": {"name": "Medium", "max_number": 50,  "attempts": 7},
    "3": {"name": "Hard",   "max_number": 100, "attempts": 7},
}

 stats = {
    "games_played": 0,
    "games_won": 0,
    "best_score": None,  # fewest attempts used in a win (None = no win yet)
}

def get_valid_number(prompt, minimum, maximum):
    """Ask the user for an integer between minimum and maximum."""
    while True:  # keep looping until we return a valid number
        user_input = input(prompt).strip()  # .strip() removes extra spaces
 
        try:
            number = int(user_input)  # fails if the text is not a whole number
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g. 7).")
            continue  # go back to the top of the loop and ask again
 
        if number < minimum or number > maximum:
            print(f"Out of range. Please enter a number from {minimum} to {maximum}.")
            continue
 
        return number  # input is valid, so give it back to the caller
    
 def show_menu():
    """Print the main menu options."""
    print("\n===== NUMBER GUESSING GAME =====")
    print("1. Play game")
    print("2. View stats")
    print("3. How to play")
    print("4. Exit")

 def choose_difficulty():
    """Ask the player to pick a difficulty and return its settings."""
    print("\nChoose a difficulty:")
    for key, level in DIFFICULTIES.items():
        print(f"{key}. {level['name']} (1-{level['max_number']}, "
              f"{level['attempts']} attempts)")
 
    choice = get_valid_number("Enter 1, 2 or 3: ", 1, 3)
    return DIFFICULTIES[str(choice)]  # look up the settings by key

# STEP 2:The game itself

def play_game():
    """Play one round of the guessing game and update the stats."""
    level = choose_difficulty()
    secret = random.randint(1, level["max_number"])  # computer's secret number
    attempts_left = level["attempts"]
    attempts_used = 0
    won = False
 
    print(f"\nI'm thinking of a number between 1 and {level['max_number']}.")
    print(f"You have {attempts_left} attempts. Good luck!")
 
    # Loop until the player runs out of attempts or guesses correctly
    while attempts_left > 0:
        guess = get_valid_number(
            f"\nAttempts left: {attempts_left}. Your guess: ",
            1, level["max_number"]
        )
        attempts_used += 1
        attempts_left -= 1
 
        if guess == secret:
            won = True
            print(f"Correct! You got it in {attempts_used} attempt(s)!")
            break  # stop the loop, the game is won
        elif guess < secret:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")
 
    if not won:
        print(f"\nGame over! The number was {secret}.")
 
    update_stats(won, attempts_used)

 # STEP 3: Update the stats after each game
def update_stats(won, attempts_used):
    """Record the result of a finished game."""
    stats["games_played"] += 1
    if won:
        stats["games_won"] += 1
        # Save the new best score if it's the first win or a better one
        if stats["best_score"] is None or attempts_used < stats["best_score"]:
            stats["best_score"] = attempts_used
 
 
def view_stats():
    """Display the player's stats."""
    print("\n----- YOUR STATS -----")
    print(f"Games played: {stats['games_played']}")
    print(f"Games won:    {stats['games_won']}")
    if stats["best_score"] is None:
        print("Best score:   No wins yet")
    else:
        print(f"Best score:   {stats['best_score']} attempt(s)")
 
 
def show_instructions():
    """Explain the rules."""
    print("\n----- HOW TO PLAY -----")
    print("1. Pick a difficulty level.")
    print("2. The computer chooses a secret number.")
    print("3. Guess the number. I'll tell you if you're too high or too low.")
    print("4. Win by guessing it before you run out of attempts!")
 
