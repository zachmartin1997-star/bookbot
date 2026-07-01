import sys
from stats import number_of_words, num_unique_characters,chars_dict_to_sorted_list
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
def print_report(book_path, word_count, sorted_characters):
    print (f"============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print (f"----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print( f"--------- Character Count -------")
    for char, count in sorted_characters:
        if char.isalpha():
            print(f"{char}: {count}")
    print (f"============= END ===============")
    return
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    char = num_unique_characters(text)
    sorted_char = chars_dict_to_sorted_list(char)
    print_report(book_path, word_count, sorted_char)
main()