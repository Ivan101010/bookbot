def get_book_text(filepath):
        with open(filepath) as f:
                return f.read()


def get_num_words(text):
        words = text.split()
        return len(words)

def get_num_characters(text):
        char_counts = {}

        for char in text:
                lowercase_char = char.lower()
        
                if lowercase_char in char_counts:
                        char_counts[lowercase_char] += 1
                else:
                        char_counts[lowercase_char] = 1

        return char_counts

def sort_dict(char_counts):
        chars_list = []

        for char, count in char_counts.items():
                char_dict = {"char": char, "count": count}
                chars_list.append(char_dict)
        
        def sort_on(dict):
                return dict["count"]

        chars_list.sort(reverse=True, key=sort_on)

        return chars_list

