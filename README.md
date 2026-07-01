# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot now accepts a book path as a command-line argument instead of using a hardcoded file. It uses Python’s sys module to read sys.argv, checks that a path was provided, and exits with a helpful usage message if not. This makes the tool flexible enough to analyze any supported book file passed in from the terminal.