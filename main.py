def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    
    number_of_words = get_number_of_words(file_contents)
    print("\n--- Beginning report of books/frankenstein.txt ---")
    print(f"\nThere are {number_of_words} words in this book.\n")

    number_of_letters = get_number_of_letters(file_contents)
    # print(f"\nLetter count: \n{number_of_letters}")
    for item in number_of_letters:
        print(f"The '{item['char']}' character was found {item['count']} times")
    
    print("\n--- End report ---")

def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_number_of_letters(text):
    letters = {}
    
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    
    letter_list = [{"char": letter, "count": count} for letter, count in letters.items()]
    letter_list.sort(key=lambda x: x["count"], reverse=True)
    
    return letter_list


if __name__ == "__main__":
    main()