import sys

from stats import get_num_words, get_char_count, sort_on, sorted_char_count_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def print_report(book_path, words, sorted_char):
    print(f"""============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\nFound {words} total words\n--------- Character Count -------""")
    for s_char in sorted_char:
        if s_char['char'].isalpha():
                       print(f"{s_char['char']}: {s_char['count']}")
    print("============= END ===============")

def main():
    book_path = sys.argv[1] 
    with open(book_path) as f:
       text = f.read()
    words = get_num_words(text)
    char =  get_char_count(text)
    sorted_char = sorted_char_count_dict(char)
    print_report(book_path, words, sorted_char)


main()
