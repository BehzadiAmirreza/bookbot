from stats import get_num_words, count_characters

def get_book_text(path_to_file):
    """Reads a text file and returns its contents as a string."""
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)

    '''''
    word_count = get_num_words(text)
    print(f"{word_count} words found in the document")
    '''''

    char_counts = count_characters(text)
    print(char_counts)

# Call main to execute the program
if __name__ == "__main__":
    main()
