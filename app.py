import streamlit as st

from logic_utils import (
    get_range_for_difficulty,
    get_attempt_limit,
    new_secret,
    attempts_left,
    is_out_of_attempts,
    parse_guess,
    update_score,
    check_guess,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit = get_attempt_limit(difficulty)

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# FIX: single source of truth for resetting a game. Used both on first load and
# by the New Game button so the two paths can never drift apart.
def start_new_game():
    # FIX (#4): remember which difficulty this secret belongs to, so we can tell
    # when the user switches and re-seed accordingly.
    st.session_state.active_difficulty = difficulty
    # FIX (#4): generate the secret from the CURRENT range (logic lives in logic_utils).
    st.session_state.secret = new_secret(difficulty)
    # FIX (#3): reset attempts to 0 so "Attempts left" can't go negative after a switch.
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.score = 0
    # FIX (#2): bump the game id; the input widget key depends on it (see form below),
    # so incrementing it clears the guess box on a new game / difficulty change.
    st.session_state.game_id = st.session_state.get("game_id", 0) + 1


# FIX (#3, #4): previously the secret/attempts were seeded only once, so changing
# difficulty mid-game left a stale out-of-range secret and a negative attempt count.
# Re-seed on first load AND whenever the selected difficulty differs from the active one.
if "secret" not in st.session_state or st.session_state.get("active_difficulty") != difficulty:
    start_new_game()

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempts_left(attempt_limit, st.session_state.attempts)}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

# FIX (#6): a plain text_input + button never reacted to the Enter key. An st.form
# submits when Enter is pressed in any of its inputs, so Submit now works on Enter.
# FIX (#2): the form key includes game_id, and clear_on_submit empties the box after
# each guess as well as on a new game (game_id changes -> new widget -> empty input).
with st.form(f"guess_form_{st.session_state.game_id}", clear_on_submit=True):
    raw_guess = st.text_input("Enter your guess:")
    submit = st.form_submit_button("Submit Guess 🚀")

# New Game and the hint toggle stay OUTSIDE the form (a form may only contain
# form_submit_button-style buttons).
col1, col2 = st.columns(2)
with col1:
    new_game = st.button("New Game 🔁")
with col2:
    show_hint = st.checkbox("Show hint", value=True)

# FIX (#2): reuse start_new_game() so the button fully resets state and clears the
# input. The old version regenerated the secret but left the UI/input untouched.
if new_game:
    start_new_game()
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if is_out_of_attempts(st.session_state.attempts, attempt_limit):
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
