from __future__ import print_function
import numpy as np
import re
import sys
import argparse


def create_colors(regexes):
    """
    Creates a colors array for the regexes.

    Args:
        regexes (list): List of regex to provide colors for

    Returns:
        list: A list of colors that minimum has colors for each regex in regexes
    """
    colors = [31, 32, 33, 34, 35, 36]
    return colors * int(np.ceil(len(regexes) / len(colors)))


def grep(filename, regexes, colors, highlight):
    """
    Performs the grep operation on the given 'filename'.

    Args:
        filename (str): Filename with contents to perform grep on
        regexes (list): List of regex to look for
        colors (list): List that will be used if the regex is to be colored
        highlight (bool): To color, or not?
    """
    with open(filename, 'r') as infile:
        for line in infile:
            print_line = False

            for i in range(len(regexes)):
                if re.search(regexes[i], line):
                    print_line = True

                    if highlight:
                        offset = 0
                        for match in re.compile(regexes[i]).finditer(line):
                            line = line[:match.start() + offset] + "\033[{}m".format(colors[i])\
                                + line[match.start() + offset:match.end() + offset]\
                                + "\033[0m" + line[match.end() + offset:]
                            offset += 9
            if print_line:
                print(line.rstrip())


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
                        type=str,
                        help="filename of the file to run the grep-like utility on")
    parser.add_argument("regex",
                        type=str,
                        nargs='+',
                        help="regular expression to look through file for.")
    parser.add_argument("--highlight",
                        action="store_true")
    args = parser.parse_args()

    colors = create_colors(args.regex)
    grep(args.filename, args.regex, colors, args.highlight)
