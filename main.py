import sys
from stats import get_num_words, count_characters, sorted_list

def get_book_text(path_to_file):
    """Reads a text file and returns its contents as a string."""
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]  # Get book path from command line
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    # Count words
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")

    # Count characters
    char_counts = count_characters(text)
    sorted_chars = sorted_list(char_counts)

    print("--------- Character Count -------")
    for char, count in sorted_chars:
        print(f"{char}: {count}")

    print("============= END ===============")

# Call main to execute the program
if __name__ == "__main__":
    main()
