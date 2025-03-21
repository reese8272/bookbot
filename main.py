from stats import get_num_words, get_num_char
from collections import defaultdict
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    num_char = get_num_char(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in num_char:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == '__main__':
    main()