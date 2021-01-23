import numpy as np


class Complex:


    def __init__(self, real_part, imag_part):
        """Initialize a number with a real and complex part"""
        self.real = real_part
        self.imag = imag_part


    def __str__(self):
        """String formatting for printing"""
        if self.imag > 0:
            return ("%i + %ii" % (self.real, self.imag))
        elif self.imag < 0:
            return ("%i - %ii" % (self.real, np.abs(self.imag)))


    def __repr__(self):
        """repr formatting"""
        return ('{}({!r}, {!r})'.format(
            self.__class__.__name__,
            self.real, self.imag
            )
        )


    def __eq__(self, other):
        """Returns True if two complex numbers are equal, False else"""
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False


    # Assignment 3.3
    def __add__(self, other):
        """Returns the sum of two complex numbers"""

        #Complex
        if isinstance(other, Complex):
            real = self.real + other.real
            imag = self.imag + other.imag
            return Complex(real, imag)


        #complex
        elif isinstance(other, complex):
            real = self.real + other.real
            imag = self.imag + other.imag
            return Complex(real, imag)


        #int
        elif isinstance(other, int):
            real = self.real + other.real
            imag = self.imag + 0
            return Complex(real, imag)


        else:
            print("Not valid for addition")
            return None


    def __sub__(self, other):
        """Returns the difference of two complex numbers"""

        # Complex
        if isinstance(other, Complex):
            real = self.real - other.real
            imag = self.imag - other.imag
            return Complex(real, imag)


        # complex
        elif isinstance(other, complex):
            real = self.real - other.real
            imag = self.imag - other.imag
            return Complex(real, imag)


        # int
        elif isinstance(other, int):
            real = self.real - other.real
            imag = self.imag - 0
            return Complex(real, imag)


        else:
            print("Unknown variable type for subtraction.")
            return None


    def __mul__(self, other):
        """Returns the complex product of two numbers"""


        # Complex
        if isinstance(other, Complex):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex(real, imag)


        # complex
        elif isinstance(other, complex):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.real + self.imag * other.real
            return Complex(real, imag)


        # int
        elif isinstance(other, int):
            real = self.real * other
            imag = self.imag * other
            return Complex(real, imag)


        else:
            print("Not valid for multiplication")
            return None


    def conjugate(self):
        """Returns complex conjugate of a complex number"""
        return Complex(self.real, -self.imag)


    def modulus(self):
        """Returns the modulus of a complex number"""
        return (np.sqrt(self.real**2 + self.imag**2))


    def __radd__(self, other):
        """Executes _add_ and returns the value"""
        return self.__add__(other)


    def __rsub__(self, other):
        """Reversed __sub__() method"""
        # Complex
        if isinstance(other, Complex):
            val = other.value - self.value
            return Complex(val[0], val[1])

        # complex
        elif isinstance(other, complex):
            val = [other.real, other.imag] - self.value
            return Complex(val[0], val[1])

        # int
        elif isinstance(other, int):
            val = [other, 0] - self.value
            return Complex(val[0], val[1])

    def __rmul__(self, other):
        """Returns value given from _mul_"""
        return self.__mul__(other)


    def __complex__(self):
        """Returns self in the form of a complex object"""
        return complex(self.value[0], self.value[1])
