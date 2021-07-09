# Using pre-commit

[pre-commit framework](https://pre-commit.com/) is a great tool for ensuring new commits meet code quality standards before they get pushed to the remote repo. Hooks are defined in [`.pre-commit-config.yaml`](../.pre-commit-config.yaml) and are run automatically on any files that are added to a commit (but not untracked files).

Pre-commit is installed to the Python environment automatically along with `dev-requirements.txt`, but it must also be installed as a Git hook. To do so:

1. Activate the virtual environment
2. Run `pre-commit install` from the shell.

That's it! The hook is installed into the repo and you're good to go.

To test it out, run it against all files in the repo like so:

```bash
pre-commit run --all-files
```

Any failed checks will prevent a commit from being written, and adjustments must be made to code (and staged in the commit again) in order to pass those checks.

**Changes that do not pass pre-commit checks will not pass code review by the event team**. Adjustments to the hook code should not be necessary by any means.

For specific details on what the hooks do and what a specific error you see means, please reach out to G.
