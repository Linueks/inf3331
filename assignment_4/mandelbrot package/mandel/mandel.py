from __future__ import division, print_function
import time as time
import numpy as np
import matplotlib.pyplot as plt
import sys
from numba import jit


def compute_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations=1000, plot_filename=None):


    @jit
    def mandelbrot(z, max_iterations):


        c = z
        for n in range(max_iterations):
            if abs(z) > 4:
                return n
            z = z * z + c


        return max_iterations


    @jit
    def generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations):


        real = np.linspace(r_min, r_max, width)
        imag = np.linspace(i_min, i_max, height)
        iterations = np.zeros((width, height))

        for i in range(width):
            for j in range(height):
                iterations[i, j] = mandelbrot(real[i] + 1j * imag[j], max_iterations)

        iterations[iterations == max_iterations] = 0


        return iterations


    def plot(iterations, r_min, r_max, i_min, i_max, width, height, plot_filename=False):


        ticks = np.arange(0, width, 3 * width / 10)
        r_ticks = r_min + (r_max - r_min) * ticks / width
        i_ticks = i_min + (i_max - i_min) * ticks / height


        plt.xticks(ticks, r_ticks)
        plt.yticks(ticks, i_ticks)


        iterations = np.swapaxes(iterations, 0, 1)
        coloring = np.zeros((height, width, 3))
        coloring[:, :, 0] = np.sin(iterations[:, :])**2
        coloring[:, :, 1] = np.cos(iterations[:, :])**2
        coloring[:, :, 2] = np.sin(iterations[:, :]) * np.cos(iterations[:, :])
        #plt.hsv()
        plt.imshow(coloring)#, norm=norm)

        if isinstance(plot_filename, str):
            plt.savefig(plot_filename)

        plt.show()


    iterations = generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations)
    plot(iterations, r_min, r_max, i_min, i_max, width, height, plot_filename)


if __name__=='-__main__':
    compute_mandelbrot(-2, 1, -1.25, 1.25, 800, 600, plot_filename="testing")
