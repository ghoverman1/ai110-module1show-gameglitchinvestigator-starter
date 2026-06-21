# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game launched easily in the terminal; it was a number-guessing game that contained three difficulty levels. The website also has a developer section that assists with debugging 
- List at least two concrete bugs you noticed at the start  
1. The higher/lower hints were reversed — lower showed when it should say higher and vice versa.

2. The New Game button didn't reset the UI or re-enable the input field, even though a new number was generated.

3. Switching difficulty mid-game caused the attempt counter to go negative.

4. Changing difficulty didn't update the secret number or the "Guess a number between" text on screen.

5. Normal (1–50) and Hard (1–100) would make more sense difficulty-wise than the current setup.

6. Pressing Enter had no effect; players had to manually click Submit Guess each time.

7. The attempt counter starts at 1 instead of 0 before any guess is made.



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 13| go lower | go higher | none |
|switched game mode | new game is created| #of attemps change| none|
| new game | attempts to 0 and a new # history of guesses cleared| nothing happens | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  For this project, I used Claude as my primary AI tool throughout development. I used the Plan mode, which let me connect it directly to my codebase so it could read through the files and pinpoint issues based on the bugs I described. When making changes and Chat mode when I needed a more focused explanation of specific functions or logic I wasn't fully grasping.
  
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  A good example was the bug in which the attempt counter started at 1 before any guesses had been made. I described the issue to Claude, and it pointed out that the counter was being initialized at the wrong value in the session state setup. I checked the relevant section of code and confirmed that the initial value was indeed set to 1 rather than 0, and after updating it the counter behaved correctly from the start.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I asked Claude to help implement a fix, it placed the new code directly inside app.py when it should have been written in the separate logic file instead. This went against the structure of the project, where app.py handles routing and the logic file is meant to contain the game mechanics. I caught this by reviewing where similar functions were already defined and noticed the AI had ignored the existing separation of concerns. I had to manually move the code into the correct file and adjust the import to get everything working properly.



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  My approach was to deliberately repeat whatever action triggered the bug originally and see if the problem still occurred after my changes. If the same steps no longer produced the broken behaviour, I was confident the fix had worked. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
When I first tried running the tests in test_game_logic.py, I immediately hit an ImportError — the module couldn't find logic_utils, which meant the test file wasn't able to import the check_guess function at all. This told me that the test wasn't being run from the correct directory, so Python had no idea where to look for the logic_utils module. Once I fixed the path issue and ran the tests again, they executed properly and I was able to see which parts of the game logic were passing and which were failing, giving me a much clearer picture of where the bugs actually lived in the code.
- Did AI help you design or understand any tests? How?
Yes, when I was writing tests for the check_guess function I asked Claude what scenarios I should actually be covering. I had only written a basic test for a correct guess and wasn't thinking much beyond that. It pointed out that I should also be testing when the guess is too high and when it's too low as separate cases, which sounds obvious in hindsight but I hadn't considered structuring them that way. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit is like an over-eager chef who completely wipes the kitchen clean and throws away all active pots and pans every single time you change your mind about an ingredient. Because of this constant resetting, the chef instantly suffers from "amnesia" and forgets what you ordered or what steps they just completed. To fix this, Session State acts like a secure holding tray on the counter where the chef can safely set aside your cooked ingredients before wiping the kitchen clean. When the kitchen resets, the chef simply grabs your food right back off that holding tray so they can finish your meal without starting from scratch.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  One habit I want to carry forward is writing tests early before the bugs pile up. Having tests in place meant I could make a fix and immediately confirm it worked rather than just guessing, and that saved a lot of back and forth time. Also doing the project in advance. 

  
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently is give the AI more specific context upfront instead of just describing the symptom. A lot of the unhelpful suggestions I got were because I wasn't giving it enough information about the project structure, so the AI was basically guessing just as much as I was.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realise that AI code needs to actually be read and understood before you use it, because it can produce something that looks completely fine but is either solving the wrong problem or quietly breaking something else. You have to know enough about the code yourself to catch those mistakes, otherwise you're just swapping one bug for another.
