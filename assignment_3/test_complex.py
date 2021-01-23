import numpy as np
from my_complex import Complex


def test_addition():
    assert (Complex(1, 4) + Complex(5, -6)) == Complex(6, -2)


def test_subtraction():
    assert (Complex(1, 4) - Complex(5, -6)) == Complex(-4, 10)


def test_multiply():
    assert (Complex(-1, -4) * Complex(-5, -6)) == Complex(-19, 26)
    assert (Complex(0, 1) * Complex(0, 1)) == Complex(-1, 0)


def test_conjugation():
    assert Complex(-1, 4).conjugate() == Complex(-1, -4)


def test_modulus():
    assert Complex(3, 4).modulus() == 5


test_addition()
test_subtraction()
test_multiply()
test_conjugation()
test_modulus()
