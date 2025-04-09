import sys
from stats import get_book_text, get_num_words, get_num_characters, sort_dict

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Path to the book
    book_path = sys.argv[1]
    
    # Get the book text
    book_text = get_book_text(book_path)
    
    # Get word count (update the function call to pass book_text)
    word_count = get_num_words(book_text)
    
    # Get character counts
    char_counts = get_num_characters(book_text)
    
    # Sort the character counts
    sorted_chars = sort_dict(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character count (alphabetical only)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()