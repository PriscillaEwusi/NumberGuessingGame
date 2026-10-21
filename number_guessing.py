
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