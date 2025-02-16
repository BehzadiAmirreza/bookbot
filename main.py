def get_num_words(text):
    # Split the text into words and count the number of words
    words = text.split()
    return len(words)

def get_book_text(path):
    # Read the content of the book from the file and return it as a string
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def count_char_frequency(text):
    # Create an empty dictionary to store character frequencies
    char_frequency = {}
    
    # Convert text to lowercase to avoid duplicates
    text = text.lower()
    
    # Loop through each character in the text
    for char in text:
        # Only count alphabet characters
        if char.isalpha():
            # If the character is already in the dictionary, increment its count
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                # Otherwise, add the character to the dictionary with count 1
                char_frequency[char] = 1
            
    return char_frequency

def print_report(word_count, char_frequency):
    # Begin the report
    print(f"--- Begin report of books/frankenstein.txt ---\n")
    print(f"{word_count} words found in the document\n")
    
    # Convert char_frequency dictionary to a sorted list of tuples by frequency
    sorted_char_frequency = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Loop through sorted characters and print their counts
    for char, count in sorted_char_frequency:
        print(f"The '{char}' character was found {count} times")
    
    # End the report
    print("\n--- End report ---")

def main():
    # Path to the book file
    path_to_file = "books/frankenstein.txt"
    
    # Get the book text
    book_text = get_book_text(path_to_file)
    
    # Get the word count from the book text
    word_count = get_num_words(book_text)
    
    # Get the character frequency from the book text
    char_frequency = count_char_frequency(book_text)
    
    # Print the report
    print_report(word_count, char_frequency)

# Call the main function
if __name__ == "__main__":
    main()
