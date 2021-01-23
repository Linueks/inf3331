# Assignment 3 code
# wc.py

Simple script with the purpose of counting the lines, words, and characters of a file or files. The result of the script is printed as: [lines, words, chars, filename]

Usage:

Single file: python wc.py "filename"

All files in directory: python wc.py "\*"

All python files in directory: python wc.py ".py"

File used for testing: textfile.txt [5, 7, 28]

# my_complex.py

Contains the Complex class for basic handling of complex numbers. Contains methods for addition, subtraction, multiplication, conjugation and modulus.

Usage:

To initialize a complex number: z = Complex(1, 2). This number can now be printed: print(z) -> "1 + 2i". Addition, subtraction and multiplication can be used as expected for python numbers.

There is also functionality for complex conjugation with the conjugate method (conj = z.conjugate()), and for getting the norm (modulus) with the modulus method (norm = z.modulus())

# test_complex.py

test script for the methods implemented in the Complex class. Five test functions in total: test_addition(), test_subtraction(), test_multiply(), test_conjugation(), test_modulus(). All are called when the file is run as: python test_complex.py
