# Riddle Game
A simple guessing game, that is not really meant to be won by conventional means.<br>

## Purpose
To establish a relationship between the USER and a denizen of 'the box' (that I will refer to as AI for simplicity sake.) This game would be less about the game itself (solving riddles) and more about the dialogue from the AI to provide a sense of personality.

## How it would work
The AI would introduce itself, and the riddle game to the USER on a MAIN SCREEN. It would then offer the USER two difficulties to choose from:<br>
-EASY (which would be a limited number of simple riddles)<br>
-IMPOSSIBLE (which would be scripted events that are not meant to be directly solved, but instead be humorous and entertaining and provide HINTS to the USER)<br>

Once the USER has gone through all the scripted events they should have enough information to solve the puzzle. At this point the USER will be taken back to the MAIN SCREEN but the prompts will be different. There will now be a new prompt at the end of the EASY difficulty riddles. The answer to this riddle would be a KEYWORD that should be inferred from the previous HINTS. Which I'm thinking could be HOPE because that was all that was left in the box after Pandora opened it.


## Sample Event
I created a sample event to give you an idea of what dialogue might look like. Honestly it is pretty bare bones for now. I have some ideas for more sample events, and they would probably make more sense if they build off each other and there are more oppurtunities for dialog. I kept this one pretty lightweight just to see if this is something we would be interested in implementing or exploring. It would also need to be changed to fit the technical frameworks we want to work in. I just used pyinput plus because it was something I am familiar with, and allowed me to easily get an idea of the ground to pitch to yall.

## Implementations of prompt_toolkit
-use keybindings to throw curveballs <br>
-change AI text colors<br>
-track prompts using session<br>
-using lexers to aid in providing HINTS<br>
-reimplement idea entirely using screens buffers etc <br>
