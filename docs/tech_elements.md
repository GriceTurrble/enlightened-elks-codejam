# Tech elements

## Prompt toolkit

Prompt toolkit has a number of neat features to build full-screen applications and complex TUI programs.

### Formatted output

> Reference: [Printing (and using) formatted text](https://python-prompt-toolkit.readthedocs.io/en/master/pages/printing_text.html)

Personally would recommend we stick to something simple for this particular output, such as the HTML styles listed in the page.

Example:

```py
from prompt_toolkit import print_formatted_text
from prompt_toolkit import HTML

print_formatted_text(HTML("<ansired><b>Hello world!</b></ansired>"))
```

This outputs ansired coloring and bold text. We can also go deeper with styles (from examples):

```py
from prompt_toolkit.styles import Style

style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})

print_formatted_text(HTML('<aaa>Hello</aaa> <bbb>world</bbb>!'), style=style)
```

I think this is the most extensible method for writing styled text for our needs. Rich is nice in a similar way, but not nearly as flexible as PT seems to be.

### Input with validation

Briefly checked out Rich input prompts, details of which we can see here: https://rich.readthedocs.io/en/latest/prompt.html

However, Prompt Toolkit can take more complex validation rules, per example here: https://python-prompt-toolkit.readthedocs.io/en/master/pages/asking_for_input.html#input-validation

The benefit of the Prompt Toolkit method is it can validate on every key press, and will not even allow entry to proceed without a valid input. The screen does not move when an invalid input is given, even if `Enter` is pressed: the prompt simply stays firmly in place.

For our needs, we can valid stuff like expected responses and throw random messages back if the response is not accurate.

Of course we can also use Dialogs, which...

### Dialogs

Reference: https://python-prompt-toolkit.readthedocs.io/en/master/pages/dialogs.html

There's a lot of flexibility here for taking over the whole screen and asking for confirmations, inputs, selections, etc. Everything about the dialog screen can be styled to match what we want.

### Full screen

Reference: https://python-prompt-toolkit.readthedocs.io/en/master/pages/full_screen_apps.html

We'll need to go deep into this subject to make some split layouts and allow inputs on different parts of the screen while outputting on others. More details to follow, as this is a big part of the framework.

## Rich

Reference: https://rich.readthedocs.io/en/latest/

I'd like us to use Rich as a secondary element only as necessary. There are some neat things it can do, like Panels; but I would not want to use its Layout elements or have its own `print` function take over in place of PT's `print_formatted_text` method.

In any spot where we use a Rich object, I'd propose using a `console` instance and calling `console.print`. Otherwise, using the smaller `print` function, it should be renamed:

```py
from rich import print as rich_print
```

### Possible elements

- Panels: https://rich.readthedocs.io/en/latest/panel.html
  - Very simple wrapped panel output. Example:

    ```py
    from rich import print as rich_print
    from rich.panel import Panel

    rich_print(Panel.fit("[bold blue]Hello[/bold blue], [green]World!", title="Welcome", border_style="green"))
    ```

    We can skip the border style parts, fiddle with titles and backgrounds. Or we can skip those parts entirely and focus on doing similar stuff in PT.

## Asciimatics

Reference: https://asciimatics.readthedocs.io/en/stable/asciimatics.html

Lots of cool stuff we can do here. Check out samples in their GitHub for inspiration, here: https://github.com/peterbrittain/asciimatics/tree/master/samples
