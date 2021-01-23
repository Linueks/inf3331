from setuptools import setup, find_packages

setup(name = "linueks inf 3331 mandelbrot",
    version = "0.1",
    description = "package for mandelbrot image generation using basic python-, numba- and numpy-implementations",
    packages = ["mandel"],
    install_requires = [
        "numpy",
        "numba",
        "matplotlib"
        ],
    author = "linueks",
    author_email = "linueks@gmail.com",
    url = "whatever.com"
)
