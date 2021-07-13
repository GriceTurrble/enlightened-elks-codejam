"""
This module will display a snake game within the command line interface.
The user input will appear on the left and the game on the right.
"""

from prompt_toolkit import Application

app = Application(full_screen=True)
app.run()
