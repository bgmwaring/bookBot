from gooey import Gooey, GooeyParser
from argparse import ArgumentParser


def output(args=None):
    
    book_path = args.file_path
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Book report of {book_path} ---")
    print(f"{num_words} words in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End ---")


@Gooey(
        program_name="Book Bot"
)
def main():
    parser = GooeyParser()

    gp = parser.add_argument_group("Group 1")
    gp.add_argument(
        "-a",
        "--file_path",
        metavar="File Chooser",
        help="Choose a .txt file",
        widget="FileChooser",
        gooey_options=dict(wildcard="Text (.txt) | *.txt"),
    )

    args = parser.parse_args()
    output(args)


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


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


if __name__ == "__main__":
    main()