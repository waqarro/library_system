# Library System

This is a small Python library system made by Waka. It was built for a group assignment.

The program lets a user:

- see the list of books
- borrow a book
- return a book
-

## Project Files

- `main.py` - runs the program
- `models/book.py` - stores book details
- `models/user.py` - handles user actions
- `services/library.py` - manages the book list

## What You Need

- Python 3

You can check it with:

```bash
python3 --version
```

## How to Download

### Option 1: Download ZIP

1. Open the project on GitHub.
2. Click `Code`.
3. Click `Download ZIP`.
4. Extract the ZIP file.
5. Open the project folder in VS Code or in the terminal.

### Option 2: Clone with Git

```bash
git clone https://github.com/waqarro/library_system.git
cd library_system
```

## How to Run

From inside the project folder, run:

```bash
python3 main.py
```

If `python3` does not work, try:

```bash
python main.py
```

## Optional: Install Tabulate

This project  works with `tabulate`, please install it before running:

```bash
pip3 install tabulate
```

If `pip3` does not work, try:

```bash
python3 -m pip install tabulate
```

## Example Menu

```text
=== Library Menu ===
1. Show books
2. Borrow a book
3. Return a book
4. Exit
```

## Author

Made by Waka.
