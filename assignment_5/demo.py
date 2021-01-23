from __future__ import division, print_function

# first comment \n
# second comment


class Tester:
    def __init__(self, its):
        self.iterations = len(its)
        return None

    def __call__(self):
        for i in range(self.iterations):
            print('heihei \n pådeg')


def hello(arg, other_arg):
    if arg == True:
        return 1
    elif arg == True and other_arg == False:
        string1 = 'string1 test: True'
        counter = 0
        while arg == True:
            if counter >= 8:
                break
            print('Heisann')
            counter += 1
