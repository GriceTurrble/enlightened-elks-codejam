from prompt_toolkit.shortcuts import message_dialog


def main() -> None:
    """Main application"""
    diag = message_dialog(
        title="Enlightened Elks",
        text="Hello world!\nPress ENTER to quit.",
    )
    diag.run()


if __name__ == "__main__":
    main()
