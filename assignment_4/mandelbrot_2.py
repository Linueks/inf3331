from __future__ import division, print_function
import time as time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.style as style




r_min = -2.5
r_max = 0.5
i_min = -1.25
i_max = 1.25
width = 600
height = 600
max_iterations = 1000




def mandelbrot(plane, max_iterations):


    iterations = np.zeros_like(plane, dtype=int)
    z = np.zeros_like(plane)


    for n in range(max_iterations):
        current_values = np.less(z.real * z.real + z.imag * z.imag, 4.0) # same as abs(z) > 2 only both sides are squared. faster this way
        iterations[current_values] = n
        z[current_values] = z[current_values] * z[current_values] + plane[current_values]

    iterations[iterations == max_iterations - 1] = 0


    return iterations


def generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations):


    real = np.linspace(r_min, r_max, width)
    imag = np.linspace(i_min, i_max, height)
    plane = real + 1j * imag[:,None]
    print(np.shape(plane))
    iterations = mandelbrot(plane, max_iterations)


    return real, imag, iterations



def generate_image(r_min, r_max, i_min, i_max, width, height, max_iterations):

    start_time = time.time()
    real, imag, iterations = generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations)
    elapsed_time = time.time() - start_time
    print(elapsed_time)


    ticks = np.arange(0, width, 3 * width / 10)
    r_ticks = r_min + (r_max - r_min) * ticks / width
    plt.xticks(ticks, r_ticks)
    i_ticks = i_min + (i_max - i_min) * ticks / width
    plt.yticks(ticks, i_ticks)


    norm = colors.PowerNorm(0.3)
    plt.imshow(iterations, cmap='magma', norm=norm)
    plt.savefig('numpy_mandelbrot')



generate_image(r_min, r_max, i_min, i_max, width, height, max_iterations)
