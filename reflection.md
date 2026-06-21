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
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit is like an over-eager chef who completely wipes the kitchen clean and throws away all active pots and pans every single time you change your mind about an ingredient. Because of this constant resetting, the chef instantly suffers from "amnesia" and forgets what you ordered or what steps they just completed. To fix this, Session State acts like a secure holding tray on the counter where the chef can safely set aside your cooked ingredients before wiping the kitchen clean. When the kitchen resets, the chef simply grabs your food right back off that holding tray so they can finish your meal without starting from scratch.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
