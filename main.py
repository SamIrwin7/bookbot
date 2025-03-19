from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    text = get_book_text(sys.argv[1])
    list = split_text(text)
    num_words = len(list)
    dictionary = character_count(text)

    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")
    sorted_dict = sorted_dictionary(dictionary)



main()