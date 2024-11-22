from collections import Counter

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def word_count(text):
    words = text.split()
    word_count = Counter(words)
    return word_count

def print_most_common(word_count, numb_words=5):
    words = word_count.keys()
    for word, frew in most_common:
        print(f'{word}: {freq}')


if __name__ == "__main__":
    text = read_file('textfile.txt')
    word_count = word_count(text)
    print_most_common(word_count)