# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
there really is no point other than to waste time guessing a random number
- [ ] Detail which bugs you found.
Inverted Higher/Lower Hints - When a guess was lower than the secret number the game told the user to go lower, and when the guess was higher it told them to go higher. The condition logic inside the check_guess function had the comparisons flipped.

New Game Button Not Resetting the UI - Clicking New Game generated a new secret number in the background but the screen stayed frozen on the previous game state. The input field also became unresponsive, making it impossible to continue playing without refreshing the page.

Attempt Counter Going Negative - When switching between difficulty levels mid-game the attempt counter was not being properly reset, causing it to continue counting down past zero into negative numbers.

Difficulty Switch Not Updating Secret Number or Text - Changing the difficulty level mid-session left the original secret number in place even though the range and attempt limit changed. The welcome text displaying the number range also stayed stuck on the previous difficulty's values.

Enter Key Not Submitting Guess - Pressing Enter after typing a number into the input field did nothing. The only way to submit a guess was by clicking the Submit Guess button with the mouse.

Attempt Counter Starting at 1 - Before any guess had been made the attempt counter already displayed 1, when it should have started at 0 and only incremented after an actual guess was submitted.
- [ ] Explain what fixes you applied.
Inverted Higher/Lower Hints - Went into the check_guess function in logic_utils.py and swapped the conditions so that when the guess is less than the secret number it returns "Go Higher" and when the guess is greater it returns "Go Lower".

New Game Button Not Resetting the UI - Fixed the session state reset logic so that when New Game is clicked it properly clears and reinitialises all the relevant session variables, which forces the UI to re-render with a fresh game state and re-enables the input field.

Attempt Counter Going Negative - Added a proper reset of the attempt counter whenever the difficulty level is changed so it starts fresh from the correct limit rather than continuing to decrement from wherever it left off.

Difficulty Switch Not Updating Secret Number or Text - Updated the difficulty change handler to generate a brand new secret number within the new range whenever the difficulty is switched and also made sure the hint text on screen pulls the updated range values so it reflects the correct difficulty.

Enter Key Not Submitting Guess - Added a keyboard event listener so that pressing Enter inside the input field triggers the same submission logic as clicking the Submit Guess button.

Attempt Counter Starting at 1 - Changed the initial value of the attempt counter in the session state from 1 to 0 so it correctly starts at zero before any guess has been made.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

User selects "Normal" difficulty and the game starts with a range of 1 to 50
User enters a guess of 25 -> Game returns "Go Higher"
User enters a guess of 38 -> Game returns "Go Lower"
User enters a guess of 31 -> Game returns "Go Higher"
User enters a guess of 35 -> Game returns "Correct!"
Attempt counter updates accurately after each guess
Score is recorded and displayed on screen
User clicks New Game and the board resets cleanly for a fresh round

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

eorgehoverman@Georges-MacBook-Pro ai110-module1show-gameglitchinvestigator-starter % pytest
========================================================================== test session starts ===========================================================================
platform darwin -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/georgehoverman/ai110-module1show-gameglitchinvestigator-starter
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.14.0
collected 3 items                                                                                                                                                        

tests/test_game_logic.py ...                                                                                                                                       [100%]

=========================================================================== 3 passed in 0.01s ============================================================================
georgehoverman@Georges-MacBook-Pro ai110-module1show-gameglitchinvestigator-starter % 

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
