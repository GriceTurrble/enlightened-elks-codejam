# Visual Studio Code recommended settings

If you are using **Visual Studio Code** as your IDE of choice, here are some suggestions for settings to make life a bit easier.

## Code formatting automatically with Black

to `black` by adding the following to your settings (recommend at the workspace level unless you intend to use `black` in every project):

```jsonc
{
  "python.formatting.provider": "black"
}
```

You will need to `pip install black` into your local virtual environment in order to use it, and let VS Code know where to locate that interpreter. Details can be found here: [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).

## Linting with flake8

VS Code by default sets up `pylint` as its chosen linter, but you can easily change this to use `flake8` by changing the following two settings:

```jsonc
{
  "python.linting.flake8Enabled": true,
  "python.linting.pylintEnabled": false,
}
```

## Language server Pylance

Pylance is a language server that helps with auto imports, auto complete, object definitions, and so on. It comes packed up within the larger [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

You can install the above extension into VS Code, and tell VS Code to use Pylance with setting:

```jsonc
{
  "python.languageServer": "Pylance",
}
```

This may be done for you automatically when you first touch a Python file. If not, feel free to set it manually and then reload your editor to ensure it takes effect.

## Python editor rulers

You can set language-specific settings to adjust how the editor looks and feels. One of the easiest is rulers, which throw a vertical line into the editor at a specified column. This can aid in visibility of where your code may be getting too long.

The Jam allows up to 119 chars, while Black defaults to 88. You can add both in settings like so:

```jsonc
{
  "[python]": {
    "editor.rulers": [88, 119]
  },
}
```

## Whitespace trimming and trailing newlines

A number of settings put together can automate the process of cleaning up files for trailing whitespace and newlines:

```jsonc
{
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.trimFinalNewlines": true,
}
```

- `trimTrailingWhitespace` will omit spaces and tabs at the end of lines when you save a file, so there's less chance of introducing extra git diffs than necessary.
- `insertFinalNewline` will ensure that one blank newline exists at the end of a file, inserting one if necessary. This is a good standard practice to follow.
- `trimFinalNewlines` will trim off extra newlines, if there are more than the final blank one. So, if you accidentally hit Enter a dozen times before saving the file, this will trim those up to just one blank newline.
