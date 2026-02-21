import sys
from pathlib import Path


# Grab the book filename from the command line
if len(sys.argv) == 2:
    book = sys.argv[1]
else:
    sys.exit("Usage: python3 script32.py book.txt")


def print_dialog(dialog):
    dialog = dialog.strip()  # Remove leading/trailing whitespace

    if dialog != "" and dialog[0] == '"':
        dialog = dialog[1:]  # Remove a leading quote if present

    if dialog != "" and dialog[-1] == '"':
        dialog = dialog[:-1]  # Remove a trailing quote if present

    if dialog != "" and dialog[-1] == ",":
        dialog = dialog[:-1] + "."  # Replace trailing comma with period

    if dialog != "":
        print()
        print('ACTOR: "' + dialog + '"')


book_path = Path("txts") / book

with book_path.open(encoding="utf-8") as my_open_book:
    text = my_open_book.read()

dialog = []
inside_dialog = False

# Parse character-by-character so we only capture text between quotes.
for char in text:
    if char == '"':
        if inside_dialog:
            print_dialog("".join(dialog))
            dialog = []
            inside_dialog = False
        else:
            inside_dialog = True
            dialog = []
        continue

    if inside_dialog:
        dialog.append(char)

print("\nThe End.")
