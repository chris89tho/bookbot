def main():
    get_path = "/home/bob/workspace/github.com/chris89tho/bookbot/books/frankenstein.txt"
    text = get_book_text(get_path)
    total = get_num_words(text)
    lower_text = lower_case(text)
    letters = letter_count(lower_text)
    sorted_letters = sort_dic(letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total} words found in the document")
    print()
    for i in sorted_letters:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def lower_case(text):
    return text.lower()

def letter_count(text):
    my_dic =  {"a" : 0,
               "b" : 0,
               "c" : 0,
               "d" : 0,
               "e" : 0,
               "f" : 0,
               "g" : 0,
               "h" : 0,
               "i" : 0,
               "j" : 0,
               "k" : 0,
               "l" : 0,
               "m" : 0,
               "n" : 0,
               "o" : 0,
               "p" : 0,
               "q" : 0,
               "r" : 0,
               "s" : 0,
               "t" : 0,
               "u" : 0,
               "v" : 0,
               "w" : 0,
               "x" : 0,
               "y" : 0,
               "z" : 0
    }

    for a in my_dic.keys():
        for i in text:
            if a == i:
                my_dic[a] += 1
    return my_dic

def sort_on(dict):
    return dict["num"]

def sort_dic(my_dic):
    sorted_list = []
    for ch in my_dic:
        sorted_list.append({"char": ch, "num": my_dic[ch]})
    return sorted_list




main()