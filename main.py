def main():
    path = "books/frankestein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    character_count = count_characters(text)

    alphabet_count_list = [{"character": key, "num": value} for key,value in character_count.items() if key.isalpha()]

    alphabet_count_list.sort(reverse=True, key=sort_on)

    print(f"---Begin report of {path} ---")
    print(f"{word_count} words were used in the document.")

    for letter in alphabet_count_list:
        if  letter['character'].isalpha():
            print (f" The '{letter['character']}' character was found {letter['num']} times")
    
    print("---End Report---")







def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count_dictionary = {}
    text_only = text.lower().replace(" ", "")

    for character in text_only:

        if character in count_dictionary:
            count_dictionary[character] += 1

        else:
            count_dictionary[character] = 1

    return count_dictionary

def sort_on(dict):
    return dict["num"]


main()