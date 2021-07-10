"""You must 'pip install prompt_toolkit' in order to use this.

This module prompts a user for input on one side of the terminal.
And on the other side ('reverse_user') it displays the prompt, but
mirrored.
This will show a window on the left for user input. When the user types, the
reversed input is shown on the right. Pressing Ctrl-C will quit the application.

It is more or less a copy of this:
https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/examples/full-screen/split-screen.py
"""
from typing import Any

from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, VSplit, Window, WindowAlign
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout

# 3. Create the buffers
#    ------------------

left_buffer = Buffer()
right_buffer = Buffer()

# 1. First we create the layout
#    --------------------------

left_window = Window(BufferControl(buffer=left_buffer))
right_window = Window(BufferControl(buffer=right_buffer))


body = VSplit(
    [
        left_window,
        # A vertical line in the middle. We explicitly specify the width, to make
        # sure that the layout engine will not try to divide the whole width by
        # three for all these windows.
        Window(width=1, char="|", style="class:line"),
        # Display the Result buffer on the right.
        right_window,
    ]
)


def get_titlebar_text() -> str:
    """Creates the titlebar."""
    return [
        ("class:title", " Reverse User Experiment "),
        ("class:title", " (Press [Ctrl-C] to quit.)"),
    ]


root_container = HSplit(
    [
        # The titlebar.
        Window(
            height=1,
            content=FormattedTextControl(get_titlebar_text),
            align=WindowAlign.CENTER,
        ),
        # Horizontal separator.
        Window(height=1, char="-", style="class:line"),
        # The 'body', like defined above.
        body,
    ]
)


# 2. Add Keybindings:

kb = KeyBindings()


@kb.add("c-c", eager=True)
@kb.add("c-q", eager=True)
def _(event: Any) -> None:
    """
    Pressing Ctrl-Q or Ctrl-C will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.

    Note that Ctrl-Q does not work on all terminals. Sometimes it requires
    executing `stty -ixon`.
    """
    event.app.exit()


# Now we add an event handler that captures change events to the buffer on the
# left. If the text changes over there, we'll update the buffer on the right.


def default_buffer_changed(_: Any) -> None:
    """Changes the buffer.

    When the buffer on the left changes, update the buffer on
    the right. We just reverse the text.
    """
    right_buffer.text = left_buffer.text[::-1]


left_buffer.on_text_changed += default_buffer_changed


# 3. Creating an `Application` instance
#    ----------------------------------

# This glues everything together.

application = Application(
    layout=Layout(root_container, focused_element=left_window),
    key_bindings=kb,
    # Let's add mouse support!
    mouse_support=True,
    # Using an alternate screen buffer means as much as: "run full screen".
    # It switches the terminal to an alternate screen.
    full_screen=True,
)


# 4. Run the application
#    -------------------


def run() -> None:
    """Run the interface. (This runs the event loop until Ctrl-Q is pressed.)"""
    application.run()


if __name__ == "__main__":
    run()
