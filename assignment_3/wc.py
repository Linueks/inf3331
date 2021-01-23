import sys
import os


def word_count(fn):


    with open(fn) as infile:

        lines = 0
        words = 0
        chars = 0

        for line in infile:
            lines += 1
            for word in line.split():
                words += 1
                chars += len(word)

    return lines, words, chars


if __name__=='__main__':


    if sys.argv[1] in os.listdir(os.curdir):
        try:
            filename = sys.argv[1]
            lines, words, chars = word_count(filename)
            print(lines, words, chars, filename)

        except TypeError:
            print("Oops! File not in directory")


    elif sys.argv[1] == '*':
        try:
            file_data = dict()
            for filename in os.listdir(os.curdir):
                lines, words, chars = word_count(filename)
                file_data[filename]=(lines, words, chars)

        except TypeError:
            print('oops')


    elif sys.argv[1] == '*.py':
        try:
            file_data = dict()
            for filename in os.listdir(os.curdir):
                if filename.endswith('.py'):
                    lines, words, chars = word_count(filename)
                    file_data[filename] = (lines, words, chars)
                else:
                    continue

        except TypeError:
            print('oops')
