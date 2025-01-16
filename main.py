from collections import defaultdict

def count_words(book):
    words = book.split()
    number_of_words = len(words)
    return number_of_words

def sort_on(dict):
    return dict["num"]

def count_chars(book):
    lowered_book = book.lower()
    letters = defaultdict(int)
    for letter in lowered_book:
        if 'a' <= letter <= 'z':
            letters[letter] += 1
    char_list = []
    for char, num in letters.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def display_char_count(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()  # Empty line for formatting
    for char_dict in char_count:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print()  # Empty line for formatting
    print("--- End report ---")

def main():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    except FileNotFoundError:
        print("Error: The file 'books/frankenstein.txt' was not found. Please check the path and try again.")
        return
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    display_char_count(word_count, char_count)

if __name__ == "__main__":
    main()
