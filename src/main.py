import argparse
import asyncio
from pathlib import Path

from prompt_toolkit import Application
from prompt_toolkit.formatted_text.pygments import PygmentsTokens
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.utils import Event

from log_content import LogContentState

BASE_DIR = Path(__file__).resolve().parent
SAMPLE = BASE_DIR.parent / "data" / "sample.log"


log_content_state = LogContentState()


# top_bar = Window(height=1)
base_text = """
Hello world

Press Ctrl-C to quit."""

output_window = Window(
    FormattedTextControl(
        base_text,
    ),
)


kb = KeyBindings()


@kb.add("c-c")
def exit_(event: Event) -> None:
    """Press Ctrl-C to quit the program."""
    event.app.exit()


@kb.add("left")
@kb.add("up")
def previous_line(event: Event) -> None:
    """Press left or up to change to previous log line."""
    log_content_state.move_to_previous()
    show_current_page()


@kb.add("right")
@kb.add("down")
def next_line(event: Event) -> None:
    """Press left or up to change to next log line."""
    log_content_state.move_to_next()
    show_current_page()


@kb.add("f")
def first_line(event: Event) -> None:
    """Press f to change to first log line."""
    log_content_state.move_to_first()
    show_current_page()


@kb.add("l")
def last_line(event: Event) -> None:
    """Press l to change to last log line."""
    log_content_state.move_to_last()
    show_current_page()


body = HSplit(
    children=[
        output_window,
    ],
    padding=1,
    padding_char="-",
    key_bindings=kb,
)


layout = Layout(body)


# Main application object
application = Application(
    layout=layout,
    full_screen=True,
)
"""Main app object.

Defined in global scope here so that we can check its state from other functions
(like whether or not it's running).
"""


def show_current_page(lexed: bool = True) -> PygmentsTokens:
    """Return the current log line from the logger content state."""
    output_window.content.text = log_content_state.current_line(lexed=lexed)


def get_parser() -> argparse.ArgumentParser:
    """Does a thing"""
    parser = argparse.ArgumentParser(description="JSONline log viewer")
    parser.add_argument("-f", "--file", required=False, type=Path)
    return parser


async def main() -> None:
    """Main application"""
    global current
    parser = get_parser()
    options = parser.parse_args()
    filepath = options.file  # type: Path
    if filepath and filepath.exists():
        log_content_state.load_file(filepath)
        show_current_page()

    await asyncio.gather(
        application.run_async(),
    )


if __name__ == "__main__":
    asyncio.run(main())
