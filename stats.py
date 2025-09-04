def get_num_words(text):
    """Returns the number of words in the given text string."""
    words = text.split()  # splits on whitespace by default
    return len(words)

def count_characters(text):
    """Returns a dictionary with character counts (case-insensitive)."""
    text = text.lower()  # make everything lowercase
    char_dict = {}

    for char in text:
        if char.isalpha():  # count only alphabetic characters
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict
