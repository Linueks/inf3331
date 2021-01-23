# Assignment 5
### All code was written and tested on a Lenovo Thinkpad running Fedora 28

1. **Syntax Highlighting**
For the first task the relevant file is *highlighter.py*. When running it requires three file names supplied: syntax_file, theme_file, code_file. The code reads through the code file and colors according to dictionaries created from the syntax file and theme file. The format of the syntax file should be:
(regex expression: keyword). The format of the theme file should match:
(keyword: bash color value)
    1. **Python Syntax**
    For the *Python* highlighting there are four relevant files, excluding *highlighter.py*, they are: *python.syntax, python.theme, python2.theme* and *demo.py*. The syntax file is used for both themes. For the second theme I tried making as bad a combination of colors as I could. The file
    *demo.py* contains a non-functional code meant to showcase the full theme.<br/>```> python highlighter.py python.syntax python.theme demo.py```
    1. **Favorite Language Syntax**
    For my 'favorite' other language I choose *Matlab* as this is the only other programming language that I am slightly familiar with. I tried making the keywords differ as much as possible from the *Python* keywords.<br/>```> python highlighter.py matlab.syntax matlab.theme demo.m```

1. **Grep**
In this task we were tasked with writing a basic grep-like utility in *Python*. It requires a file name to look through as well as a regular expression to look for. I ran it on *demo.py* using one of the expressions
from my *python.syntax* file. *Grep.py* also works when supplied with
multiple regular expressions.<br/>```> python grep.py demo.py def class True False if else --highlight```

1. **Superdiff**
The program *diff.py* is supplied with a source file and an altered file which it compares to work out changes in the altered file. It then outputs to a file *diff_output.txt* which is later used to highlight additions and removals. The output file has '+' or '-' added in front of the line according to whether there was a removal or addition in the new file compared to the old one. <br/>```> python diff.py diff_demo1.txt diff_demo2.txt```
    1. **Coloring Diff**
    Just using the format from the output of *diff.py* as a syntax file to color in the same way as before.<br/>```> python highlighter.py diff.syntax diff.theme diff_output.txt```
