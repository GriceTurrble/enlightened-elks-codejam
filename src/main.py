import asyncio

from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.utils import Event
from prompt_toolkit.widgets import TextArea

# top_bar = Window(height=1)
text_ = """
Hello world

For the time being, this app just screws with your inputs by periodically
erasing the first character in the buffer below, every 0.5 seconds.

This can be one of many "curveball" we can configure via some flags,
intended to mess them up while they type in their answers.

Remains to be seen exactly how this will play out, but it can be one of the ways we try
to have the user beat a puzzle while the game makes their typing more difficult.

Press Ctrl-C to quit."""

output_window = Window(
    FormattedTextControl(text_),
    style="bg:white black",
)


text_field = TextArea(
    text="...Lookit me, I'm disappearing, nooooooo!\n",
    height=3,
)
text_field.buffer.cursor_down()

root_container = HSplit(
    children=[
        output_window,
        text_field,
    ],
    padding=1,
    padding_char="-",
)

layout = Layout(root_container)


kb = KeyBindings()


@kb.add("c-c")
def exit_(event: Event) -> None:
    """Press Ctrl-C to quit the program."""
    event.app.exit()


# Main application object
application = Application(layout=layout, full_screen=True, key_bindings=kb)
"""Main app object.

Defined in global scope here so that we can check its state from other functions
(like whether or not it's running).
"""


async def throw_curveballs() -> None:
    """Periodically screw with the user's input.

    Requires the app to be running, otherwise the function will exit immediately
    (and likely the entire program will close).
    """

    def remove_first_char() -> None:
        text_field.buffer.transform_region(
            from_=0,
            to=1,
            transform_callback=lambda x: "",
        )

    while application.is_running:
        # If the app closes, stop messing with things
        await asyncio.sleep(0.5)
        remove_first_char()


async def main() -> None:
    """Main application"""
    await asyncio.gather(
        application.run_async(),
        throw_curveballs(),
    )


if __name__ == "__main__":
    asyncio.run(main())
