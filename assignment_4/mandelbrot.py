from __future__ import division, print_function
import time as time
import numpy as np
import matplotlib.pyplot as plt
import sys
from numba import jit



"""
locations

coloring:
np.sin(np.log(iterations[i, j] / 1000)), np.cos(np.log(iterations[i, j] / 1000)), np.tan(np.log(iterations[i, j] / 1000))

coloring[:, :, 0] = np.sin(np.transpose(iterations[:, :])) * (np.log(np.abs(np.transpose(iterations[:, :])) / 1000))
coloring[:, :, 1] = np.cos(np.transpose(iterations[:, :])) * (np.log(np.abs(np.transpose(iterations[:, :])) / 1000))
coloring[:, :, 2] = np.sin(np.transpose(iterations[:, :])) * (np.log(np.abs(np.transpose(iterations[:, :])) / 1000))

coloring[:, :, 0] = np.sin(iterations[:, :])
coloring[:, :, 1] = np.cos(iterations[:, :])
coloring[:, :, 2] = np.sin(iterations[:, :])**2

"""
def generate_report(r_min, r_max, i_min, i_max, width, height, max_iterations, run_time, filename=False):
    """Should save parameters and savetime for a given run"""


    if not filename:
        return

    else:
        with open(filename, 'w') as outfile:
            outfile.write("r_min = %.2f, r_max = %.2f, i_min = %.2f, i_max = %.2f, width = %i, height = %i, max_it = %i, run time = %.2f" %
                            (r_min, r_max, i_min, i_max, width, height, max_iterations, run_time))


def check_domain_intersection(r_min, r_max, i_min, i_max):
    """Function to check whether supplied domain contains parts of the mandelbrot set."""
    mandel_r_min, mandel_r_max, mandel_i_min, mandel_i_max = -2, 1, -1.25, 1.25


    if r_min > mandel_r_max or r_max < mandel_i_min:
        return False
    elif i_min > mandel_i_max or i_max < mandel_i_min:
        return False
    else:
        return True


def generate_image(iterations, r_min, r_max, i_min, i_max, width, height, filename, numpy=True):
    """Method for generating an image from a (width, height) array of mandelbrot escape values"""


    ticks = np.arange(0, width, 3 * width / 10)
    r_ticks = r_min + (r_max - r_min) * ticks / width
    i_ticks = i_min + (i_max - i_min) * ticks / height


    plt.xticks(ticks, r_ticks)
    plt.yticks(ticks, i_ticks)


    if not filename:
        if numpy == True:
            print(np.shape(iterations))
            print(type(iterations))
            coloring = np.zeros((height, width, 3))
            coloring[:, :, 0] = np.sin(iterations[:, :])**2
            coloring[:, :, 1] = np.cos(iterations[:, :])**2
            coloring[:, :, 2] = np.sin(iterations[:, :]) * np.cos(iterations[:, :])
            plt.imshow(coloring)
            plt.show()

        else:
            iterations = np.swapaxes(iterations, 0, 1)
            coloring = np.zeros((height, width, 3))
            coloring[:, :, 0] = np.sin(iterations[:, :])**2
            coloring[:, :, 1] = np.cos(iterations[:, :])**2
            coloring[:, :, 2] = np.sin(iterations[:, :]) * np.cos(iterations[:, :])
            #plt.hsv()
            plt.imshow(coloring)#, norm=norm)
            plt.show()

    else:
        if numpy == True:
            coloring = np.zeros((height, width, 3))
            coloring[:, :, 0] = np.sin(iterations[:, :])**2
            coloring[:, :, 1] = np.cos(iterations[:, :])**2
            coloring[:, :, 2] = np.sin(iterations[:, :]) * np.cos(iterations[:, :])
            plt.imshow(coloring)
            plt.savefig(filename)
            plt.show()

        else:
            iterations = np.swapaxes(iterations, 0, 1)
            coloring = np.zeros((height, width, 3))
            coloring[:, :, 0] = np.sin(iterations[:, :])**2
            coloring[:, :, 1] = np.cos(iterations[:, :])**2
            coloring[:, :, 2] = np.sin(iterations[:, :]) * np.cos(iterations[:, :])
            plt.imshow(coloring)#, norm=norm)
            plt.savefig(filename)
            plt.show()




def python_implementation(r_min, r_max, i_min, i_max, width, height, max_iterations):
    """
    Runs the basic python implementation to generate the mandelbrot
    set for an input resolution and max iterations
    """


    def mandelbrot(z, max_iterations):


        c = z
        for n in range(max_iterations):
            if abs(z) > 4:
                return n
            z = z * z + c



        return max_iterations


    def generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations):


        real = np.linspace(r_min, r_max, np.int(np.round(width)))
        imag = np.linspace(i_min, i_max, np.int(np.round(height)))
        iterations = np.zeros((width, height))

        for i in range(width):
            for j in range(height):
                iterations[i, j] = mandelbrot(real[i] + 1j * imag[j], max_iterations)

        iterations[iterations == max_iterations] = 0


        return iterations


    iterations = generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations)


    return iterations


def numpy_implementation(r_min, r_max, i_min, i_max, width, height, max_iterations):
    """
    Runs the vectorized numpy implementation to generate the mandelbrot
    set for an input resolution and max iterations
    """
    def mandelbrot(plane, max_iterations):
        """Numpy implementation of the mandelbrot set"""


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
        iterations = mandelbrot(plane, max_iterations)


        return iterations


    iterations = generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations)


    return iterations


def numba_implementation(r_min, r_max, i_min, i_max, width, height, max_iterations):
    """
    Runs the numba implementation to generate the mandelbrot
    set for an input resolution and max iterations
    """
    @jit
    def mandelbrot(z, max_iterations):
        """Same function as basic python exept with @jit in front of function"""


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


    iterations = generate_mandelbrot(r_min, r_max, i_min, i_max, width, height, max_iterations)


    return iterations


if __name__ == "__main__":
    """The script should take values for the resolution, region of complex plane, implementation version,
    output filename"""


    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        print('Usage: python mandelbrot.py r_min r_max i_min i_max width height max_iterations method output_file\n')
        print('     r min and r max are the limits for the real part of the complex plane.')
        print('     i min and i max are the limits for the imaginary part of the complex plane.')
        print('     width and height control the image resolution.\n')
        print('     The method argument accepts the keywords: "python", "numpy", "numba"')
        print('     Running the script with no arguments defaults to numba implementation')


    elif len(sys.argv) == 1:
        numba_implementation()


    elif len(sys.argv) == 9 or len(sys.argv) == 10:
        if len(sys.argv) == 10:
            filename = sys.argv[-1]
        else:
            filename = False

        r_min, r_max, i_min, i_max, width, height, max_iterations, method = sys.argv[1:9]
        r_min, r_max, i_min, i_max, width, height, max_iterations = float(r_min), float(r_max), float(i_min), float(i_max), int(width), int(height), int(max_iterations)


        if check_domain_intersection(r_min, r_max, i_min, i_max):
            if method == "numpy":
                start_time = time.time()
                iterations = numpy_implementation(r_min, r_max, i_min, i_max, width, height, max_iterations)
                run_time = time.time() - start_time
                generate_report(r_min, r_max, i_min, i_max, width, height, max_iterations, run_time, filename)
                generate_image(iterations, r_min, r_max, i_min, i_max, width, height, filename)

            elif method == "python":
                start_time = time.time()
                iterations = python_implementation(r_min, r_max, i_min, i_max, width, height, max_iterations)
                run_time = time.time() - start_time
                generate_report(r_min, r_max, i_min, i_max, width, height, max_iterations, run_time, filename)
                generate_image(iterations, r_min, r_max, i_min, i_max, width, height, filename, numpy=False)

            elif method == "numba":
                start_time = time.time()
                iterations = numba_implementation(r_min, r_max, i_min, i_max, width, height, max_iterations)
                run_time = time.time() - start_time
                generate_report(r_min, r_max, i_min, i_max, width, height, max_iterations, run_time, filename)
                generate_image(iterations, r_min, r_max, i_min, i_max, width, height, filename, numpy=False)

        else:
            print("The area of the complex plane you have specified does not contain the mandelbrot set")

    else:
        print('Use command line argument --help for usage')
