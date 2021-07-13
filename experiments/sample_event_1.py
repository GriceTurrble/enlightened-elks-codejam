import time

import pyinputplus as pyip

""" Will need to pip install pyinputplus to run!

This will be responsible for running the 'riddles in the dark' IMPOSSIBLE EVENT.

-give away a hint about 'keyword' that will 'destroy AI'
-could use tool_prompt sessions to improve with:
    -keybindings
    -session.history to check if input has been used previously.

-based off Bilbo's encounter with Gollum.
"""


# Event specific dialogues:
TALK_1 = "I suppose this is not quite a riddle, but I do indeed find it amusing."
FIRST_PROMPT = "What have I got in my pockets?"
FIRST_ANSWERS = ["string", "nothing", "precious", "hands"]
GENERIC_TAUNTS = [
    "As if.",
    "You nasty noser!",
    "What makes you think I have THOSE!",
    "Filth",
]

# MENU RESPONSES AND TAUNTS:
PRE_MENU_TAUNT = """Although I can't guarantee it (since I failed to validate them), it brings me what you might call
joy to think of your responses as amusing. Why don't I give you some help. I can assure you this time I will be
listening."""
STRING_RESPONSE = "A clever choice but wrong nonetheless. Although I do have these in the <e>literal sense<e>."
NOTHING_RESPONSE = 'An amusing choice, but INCORRECT. If not for your silly HOPE, I"d say this is all YOU have!'
# Possible allusion to HOPE/HINT
PRECIOUS_RESPONSE = "As if I would need or want such a mundane item . . ."
HANDS_RESPONSE = 'If I had them, you certainly wouldn"t find them there, that is a filthy human habit!'

# Display dialogue and ask user riddle:
print(TALK_1)
time.sleep(1)
print(FIRST_PROMPT)
time.sleep(2)

# Specify number of guesses to the user:
num_guesses = 3
print(f"I will give you {num_guesses + 1} guesses.")

for i in range(num_guesses):
    response = input(f"Guess number {i + 1}: ")
    print(GENERIC_TAUNTS[i])

    if i == (num_guesses - 1):
        response = input("Last guess: ")
        print()  # New-line.
        break

# Give USER options to choose from and taunt them:
print(PRE_MENU_TAUNT)
responses_allowed = []
while len(responses_allowed) < 4:
    response = pyip.inputMenu(FIRST_ANSWERS, numbered=True)

    # Check if response has already been tried and prevent it from being added again:
    if response in responses_allowed:
        print("That didn't work the first time . . .")
        continue

    # Handle 'string':
    if response == FIRST_ANSWERS[0]:
        responses_allowed.append(response)
        print(STRING_RESPONSE)
    # Handle 'nothing':
    if response == FIRST_ANSWERS[1]:
        responses_allowed.append(response)
        print(NOTHING_RESPONSE)
    # Handle 'precious':
    if response == FIRST_ANSWERS[2]:
        responses_allowed.append(response)
        print(PRECIOUS_RESPONSE)
    # Handle 'hands':
    if response == FIRST_ANSWERS[3]:
        responses_allowed.append(response)
        print(HANDS_RESPONSE)

# All allowed responses have been tried:
print("END OF EVENT. RETURN TO MAIN MENU.")
