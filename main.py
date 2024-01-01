def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # num_words = get_num_words(text)
    # chars_dict = get_chars_dict(text)
    print(f"--- Begin report of {book_path} ---")
    report(text)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def report(text):
    num = get_num_words(text)
    items = get_chars_dict(text).items()
    sortedChar = sorted(items, key = lambda chars: chars[1], reverse = True)
    
    print(f"{num} words found in the document")
    print()
    for ch in sortedChar:
        if (ch[0].isalpha()):
            print(f"The '{ch[0]}' character was found {ch[1]} times")
        else:
            continue

main()