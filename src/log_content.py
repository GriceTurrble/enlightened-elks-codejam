import json
from pathlib import Path
from typing import Any, List

import orjson
import pygments
from prompt_toolkit.formatted_text import PygmentsTokens
from pygments.lexers import JsonLexer


class LogLine:
    """One log entry, read in as a JSON string."""

    def __init__(self, line: str) -> None:
        self._raw = line
        self._line = None

    @property
    def line(self) -> Any:
        """Converts the raw line from JSON to Python, caches, and returns the cache."""
        if self._line is None:
            self._line = orjson.loads(self._raw)
        return self._line

    @line.setter
    def line(self, value: str) -> None:
        self._line = None
        if isinstance(value, str):
            self._raw = value
        else:
            self._raw = orjson.dumps(value)

    @line.deleter
    def line(self) -> None:
        self._line = None
        self._raw = None

    def pretty_str(
        self,
        indent: int = 2,
        sort_keys: bool = True,
    ) -> str:
        """Return an indented "pretty" string for this log line."""
        return json.dumps(self.line, indent=indent, sort_keys=sort_keys)

    def lexed_text(self) -> PygmentsTokens:
        """Do a thing."""
        tokens = pygments.lex(self.pretty_str(), lexer=JsonLexer())
        return PygmentsTokens(tokens)

    def __getitem__(self, key: Any) -> Any:
        return self.line.__getitem__(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        self.line.__setitem__(key, value)


class LogContent:
    """Converts string content from a log file into lines of JSON content."""

    def __init__(self, content: str) -> None:
        self.content = content
        self._lines = None

    @property
    def lines(self) -> List[LogLine]:
        """Processes raw lines into LogLines as needed, then returns that list."""
        if self._lines is None:
            self._lines = [LogLine(x) for x in self.content.split("\n")]
        return self._lines

    def __len__(self) -> int:
        return len(self.lines)

    def __iter__(self) -> Any:
        return self.lines.__iter__()

    def __getitem__(self, key: int) -> LogLine:
        return self.lines.__getitem__(key)

    def __setitem__(self, key: int, val: Any) -> None:
        self.lines.__setitem__(key, val)


class LogContentState:
    """Stores state of the log content view."""

    def __init__(self, filepath: Path = None):
        self.log_content = None
        self.idx = 0
        if filepath and filepath.exists():
            self.load_file(filepath)

    def load_file(self, filepath: Path) -> None:
        """Load content from a file and parse as a `LogContent` object."""
        content = filepath.read_text().strip()
        self.log_content = LogContent(content)
        self.idx = len(self.log_content) - 1

    @property
    def line_no(self) -> int:
        """Current log line number."""
        return self.idx + 1

    def current_line(self, lexed: bool = True) -> LogLine:
        """Return the current log line for output."""
        line = self.log_content[self.idx]
        line.line["_log_line"] = self.idx + 1
        if lexed:
            return line.lexed_text()
        return line

    def current_line_lexed(self) -> PygmentsTokens:
        """Returns the current log line properly lexed."""
        return self.log_content[self.idx].lexed_text()

    def move_to_previous(self) -> None:
        """Move index to the previous line"""
        self.idx -= 1
        if self.idx < 0:
            self.idx = 0

    def move_to_next(self) -> None:
        """Move index to the previous line"""
        self.idx += 1
        try:
            self.log_content[self.idx]
        except IndexError:
            self.idx = len(self.log_content) - 1

    def move_to_first(self) -> None:
        """Move index to the first line"""
        self.idx = 0

    def move_to_last(self) -> None:
        """Move index to the last line"""
        self.idx = len(self.log_content) - 1


def tester() -> None:
    """Test output from a sample log file."""
    from pathlib import Path

    sample = Path(__file__).resolve().parents[1] / "data" / "sample.log"
    content = LogContent(sample.read_text())

    print(content[0].pretty_str())
    print("-" * 50)
    print(content[1].pretty_str())


if __name__ == "__main__":
    tester()
