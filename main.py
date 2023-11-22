with open("books/frankenstein.txt") as f:
    
    file_contents = f.read()

    words = file_contents.split()
    word_count = len(words)

print(f"Word Count: {word_count}")