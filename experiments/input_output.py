"""
A simple application that reads input from the bottom, and puts it at the top.

Just made this to show how you could have a terminal that would tailor outputs based on specific inputs.
"""


from typing import Any

from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import TextArea

display_text = """
This is probably where the rules will go.

Try some keywords: 'hello', 'play snake', 'buy', 'open', 'quit
"""
input_to_output = {
    "hello": "\n\ngoodbye Stranger",
    "buy": "\n\nWhat are ya buying . . . Stranger?",
    "scv": "\n\nSCV GOOD TO GO SIR",
    "marine": "\n\nI HEEEARD YA!",
    "banshee": '\n\nI"ve got my ears on!',
    "open": "\n\nYou open the box, How mysterious!",
    "quit": '\n\nYou can"t quit now you fool!',
    "play riddles": "\n\nSTART THE RIDDLE GAME",
    "play snake": "\n\nSTART THE SNAKE GAME",
}


def get_keyword_output(input: Any) -> str:
    """Checks the dictionary for the input and returns a string to be used as output."""
    if input in input_to_output:
        return input_to_output[input]
    else:
        return "\n\nYour input was: " + input


def main() -> None:
    """The main function."""
    # The layout.

    # Define fields to go into root container:
    output_field = TextArea(
        style="class:output-field", text=display_text
    )  # This is where inputs will be displayed.
    input_field = TextArea(
        height=1,
        prompt=">>",
        style="class:input-field",
        multiline=False,
        wrap_lines=False,
    )

    root_container = HSplit(
        [
            output_field,
            Window(height=1, char="_", style="class:line"),
            input_field,
        ]
    )

    # Need to have something to accept/check input:
    def accept(buff: Any) -> str:
        # This will evaluate input.
        output = get_keyword_output(input_field.text)

        # Add checked text to output buffer:
        new_text = output_field.text + output
        output_field.buffer.document = Document(
            text=new_text, cursor_position=len(new_text)
        )

    input_field.accept_handler = accept  # This resets the input field/uses the accept

    # The key bindings.
    kb = KeyBindings()

    @kb.add("c-c")
    @kb.add("c-q")
    def _(event: Any) -> None:
        """Pressing Ctrl-Q or Ctrl-C will exit the user interface."""
        event.app.exit()

    # Style.
    style = Style(
        [
            ("output-field", "bg:#000044 #ffffff"),
            ("input-field", "bg:#000000 #ffffff"),
            ("line", "#004400"),
        ]
    )

    # Run application
    application = Application(
        layout=Layout(root_container, focused_element=input_field),
        key_bindings=kb,
        style=style,
        full_screen=True,
    )

    application.run()


if __name__ == "__main__":
    main()
