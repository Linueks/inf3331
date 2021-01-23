import argparse
import re

DEFAULT_COLOR = "\033[0m"


def syntax_dict(filename):
    """
    Reads through a supplied file: 'filename'
    with format: (syntax: keyword) populating a dictionary
    to be matched with a theme dictionary in order to color
    code example

    return: a dictionary containing the syntax data
    """

    syntax = {}
    with open(filename) as infile:
        for line in infile:
            keyword = line.split()[-1]
            value = line.split('"')[1]

            syntax[keyword] = value

    return syntax


def theme_dict(filename):
    """
    Function reads through a file: 'filename'
    with the format: (keyword: value) and populates
    a dictionary (theme) to be used when coloring
    the code sample

    return: a dictionary containing the theme data
    """

    theme = {}
    with open(filename) as infile:
        for line in infile:
            keyword = line.split(':')[0]
            value = line.split(':')[1].strip()
            theme[keyword] = value

    return theme


def highlighter(filename, syntax, theme):
    """
    inputs: code source file, syntax dictionary, theme dictionary.

    The highlighter method uses syntax and theme dictionary to color the
    code in the source file according to instructions saved in syntax and theme
    dicts.

    return: None
    """

    with open(filename) as infile:
        code = infile.read()

    color = [DEFAULT_COLOR for i in range(len(code))]                           # Array containing color for each character

    for rule in syntax:
        regex = re.compile(syntax[rule], re.MULTILINE)
        for match in regex.finditer(code):
            for i in range(match.start(), match.end()):
                color[i] = "\033[{}m".format(theme[rule])

    code = color[0] + code                                                      # Add color for first character
    offset = len(color[0])                                                      # Keep track of the offset from adding more characters
    for c in range(1, len(color)):
        if(color[c] != color[c-1]):
            code = code[:c + offset] + color[c] + code[c + offset:]             # Puts in the color code if it's different than the last color, and updates the offset

            offset = offset + len(color[c])

    code = code + DEFAULT_COLOR                                                 # Reset color to default after content
    print(code)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("syntaxfile",
                        type=str,
                        help="filename of the syntax file")
    parser.add_argument("themefile",
                        type=str,
                        help="filename of the color scheme file")
    parser.add_argument("sourcefile",
                        type=str,
                        help="filename of the source code to color")

    args = parser.parse_args()
    syntax = syntax_dict(args.syntaxfile)
    theme = theme_dict(args.themefile)

    highlighter(args.sourcefile, syntax, theme)
