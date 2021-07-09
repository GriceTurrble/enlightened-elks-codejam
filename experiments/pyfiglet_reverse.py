"""You must `pip install pyfiglet` to use this.

Pyfiglet is used as a dependency for Asciimatics, and is how
Asciimatics prints these text figures on the screen.

This module takes the default font for a Figlet, manually
mirrors some of its internal characters, and produces a
completely mirrored string of text.
"""
from pyfiglet import Figlet

BASE_CHARS = "$V([<'_)`.|-, ]/=\\>O"
MIRR_CHARS = "$V)]>'_(`.|-, [\\=/<O"
CHAR_MAP = dict(zip(BASE_CHARS, MIRR_CHARS))


def mirror_str(text: str) -> str:
    """Mirrors characters from BASE_CHARS to MIRR_CHARS.

    Requires the base font of Figlet in use; not nearly dynamic enough!
    """
    new_str = ""
    for char in text:
        new_str += CHAR_MAP[char]
    return new_str


def mirrored_fig(text: str) -> str:
    """Returns a mirrored version of a Figlet from Pyfiglet.

    This text should appear completely mirrored horizontally.
    """
    # Generate a normal Figlet
    forward = Figlet().renderText(text)

    # Mirror the forward-facing fig text
    mirrored = []
    for line in forward.split("\n"):
        new_line = line[::-1]
        mirrored.append(mirror_str(new_line))
    mirrored = "\n".join(mirrored)

    return mirrored


def main() -> str:
    """Test output."""
    text = "Hello, world!"
    # A normal figure
    print(Figlet().renderText(text))
    # A reversed one
    print(mirrored_fig(text))


if __name__ == "__main__":
    main()
