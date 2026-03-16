# Library System

This is a small Python library system made by Waka. I built it for a group assignment.

The program lets a user:

- see the list of books
- borrow a book
- return a book

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

## Requirements

This program uses a third-party Python module called **tabulate** to display the list of books in a table format.

The program will automatically try to install the required module when it starts.

However, if the automatic installation fails, please install the module manually using:

```bash
pip3 install tabulate
```

If `pip3` does not work, you can try:

```bash
python3 -m pip install tabulate
```

## Running the Program

After installing the required module, run the program with:

```bash
python3 main.py
```

## Author

Made by Waka.
[itswaka.com](https://itswaka.com)
