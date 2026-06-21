import random

# How many guesses each difficulty allows. Kept here (not in the UI) so all
# game rules live in one place.
ATTEMPT_LIMITS = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def get_attempt_limit(difficulty: str) -> int:
    """Return the number of attempts allowed for a given difficulty."""
    return ATTEMPT_LIMITS.get(difficulty, ATTEMPT_LIMITS["Hard"])


def new_secret(difficulty: str) -> int:
    """Pick a random secret number within the difficulty's range."""
    low, high = get_range_for_difficulty(difficulty)
    return random.randint(low, high)


def attempts_left(attempt_limit: int, attempts_used: int) -> int:
    """Remaining attempts, never below 0."""
    return max(0, attempt_limit - attempts_used)


def is_out_of_attempts(attempts_used: int, attempt_limit: int) -> bool:
    """True when the player has no attempts remaining."""
    return attempts_used >= attempt_limit


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#The higher/lower hints were reversed — lower showed when it should say higher and vice versa.

def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"



def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # First-try win = 100, then 90, 80, ... with a floor of 10.
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
