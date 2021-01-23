from __future__ import division, print_function
import time as time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.style as style
#style.use('ggplot')

"""Wrote docstrings in last version of program mandelbrot.py"""


r_min = -2.5
r_max = 0.5
i_min = -1.25
i_max = 1.25
width = 600
height = 600
max_iterations = 1000



def mandelbrot(z, max_iterations):


    c = z
    for n in range(max_iterations):
        if abs(z) > 4:
            return n
        z = z * z + c


    return max_iterations


def generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations):


    real = np.linspace(r_min, r_max, width)
    imag = np.linspace(i_min, i_max, height)
    iterations = np.zeros((width, height))

    for i in range(width):
        for j in range(height):
            iterations[i, j] = mandelbrot(real[i] + 1j * imag[j], max_iterations)

    iterations[iterations == max_iterations] = 0


    return real, imag, iterations


def generate_image(r_min, r_max, i_min, i_max, width, height, max_iterations):

    start_time = time.time()
    real, imag, iterations = generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations)
    #iterations[iterations == max_iterations - 1] = 0
    elapsed_time = time.time() - start_time
    print(elapsed_time)


    ticks = np.arange(0, width, 3 * width / 10)
    r_ticks = r_min + (r_max - r_min) * ticks / width
    plt.xticks(ticks, r_ticks)
    i_ticks = i_min + (i_max - i_min) * ticks / width
    plt.yticks(ticks, i_ticks)


    norm = colors.PowerNorm(0.3)
    plt.imshow(np.transpose(iterations), cmap='magma', norm=norm)
    plt.savefig('python_mandelbrot')



generate_image(r_min, r_max, i_min, i_max, width, height, max_iterations)
