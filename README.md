# Getting Started with py-git-hooks

The script needs to be executed in the project root directory and accepts the hook you want and the command you want, for example, if you want a pre-compile that does a clean everytime you commit, you would run:

    py-git-hooks pre-commit clean

If it's not gradle or maven, you can just use quotes around the command with your package manager like so:

    py-git-hooks pre-commit "npm test"
