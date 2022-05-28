# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from importlib.resources import contents
from itertools import count


def read_file_content(filename):
    with open(filename) as f:
        contents = f.read
        print(contents) 

    return contents


def count_words():
    text = read_file_content("./story.txt")
    lines = []
    with open("./story.txt") as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        count+= 1
        # print(f'line {count}: {line}')
    # return {"as": 10, "would": 20}
    return f'line {count}: {line}'