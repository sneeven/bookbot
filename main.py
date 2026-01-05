from stats import count_words, n_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    unique_char = n_char(text)
    print(f"Found {num_words} total words")
    print(unique_char)


main()