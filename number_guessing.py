
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
 
