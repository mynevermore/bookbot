def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = get_word_count(text)
    letter_count = get_letter_count(text)
    print_report(book_path, num_words, letter_count)

def print_report(book_path, num_words, letter_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    list_letters = []
    for key, value in letter_count.items():
        list_letters.append((key, value))
    list_letters.sort(key=lambda a:a[1], reverse=True)
    for tup in list_letters:
        print(f"The '{tup[0]}' character was found {tup[1]} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letters = {}

    text = text.lower()
    for letter in text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    
    return letters

main()