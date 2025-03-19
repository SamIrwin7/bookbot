def get_book_text(file_path):
    """Reads the contents of a book file and returns it as a string."""
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def split_text(file_contents):
    """Splits text into a list of words."""
    words_list = file_contents.split()  # Avoid using 'list' as a variable name
    return words_list

def character_count(file_contents):
    """Counts the frequency of each character in the text."""
    text = file_contents.lower()  # Convert text to lowercase
    character_dictionary = {}  # Initialize an empty dictionary

    for char in text:
        if char.isalpha():  # Only count letters (ignore spaces and punctuation)
            if char in character_dictionary:
                character_dictionary[char] += 1
            else:
                character_dictionary[char] = 1

    return character_dictionary  # Return dictionary with character counts

def sort_on(item):
    """Returns the frequency value for sorting."""
    return item[1]  # Sort based on character count (value, not key)

def sorted_dictionary(character_dictionary):
    """Sorts the dictionary by frequency in descending order using .sort()."""
    sorted_list = list(character_dictionary.items())  # Convert dictionary to list of tuples
    sorted_list.sort(key=sort_on, reverse=True)  # Use .sort() (in-place sorting)
    for key, value in sorted_list:
        print(f"{key}: {value}")
    return sorted_list





    

