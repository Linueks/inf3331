from __future__ import print_function
import argparse
import sys
import re


def readfile(filename):
    """
    Gets a list of lines from a file

    Args:
        filename (str): The file to be read

    Returns:
        list: A list of lines in the given file
    """

    lines = []
    with open(filename, 'r') as infile:
        for line in infile:
            lines.append(line.strip())

    return lines


def compare_files(lines1, lines2):
    """
    Compares two lists of lines and writes
    the result to diff_output.txt

    Args:
        lines1 (list): List of original lines
        lines2 (list): List of altered lines
    """

    changes = []

    for i in range(max(len(lines1), len(lines2))):
        if len(lines1) > i:
            if lines1[i] not in lines2 and lines1[i] != "":
                changes.append("- " + lines1[i])
        if len(lines2) > i:
            if lines2[i] not in lines1 and lines2[i] != "":
                changes.append("+ " + lines2[i])
            elif lines2[i] in lines1 and lines2[i] != "":
                changes.append("0 " + lines2[i])

    with open("diff_output.txt", "w") as outfile:
        outfile.writelines("\n".join(changes))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("file1",
                        type=str,
                        help="filename of the source file")
    parser.add_argument("file2",
                        type=str,
                        help="filename of the file which the source file is being compared against")

    args = parser.parse_args()

    lines1 = readfile(args.file1)
    lines2 = readfile(args.file2)
    compare_files(lines1, lines2)
