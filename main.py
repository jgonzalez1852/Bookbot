import sys
from stats import (get_book_stats, return_char_counts_all)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

get_book_stats(book_path)
char_counts = return_char_counts_all(book_path)

for char in char_counts:
    if char["char"].isalpha():
        print(f'{char["char"]}: {char["num"]}')