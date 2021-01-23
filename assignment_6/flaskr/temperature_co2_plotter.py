import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
plt.style.use('ggplot')


def plot_temperature(data, time_min, time_max, months, temp_min=None, temp_max=None):
    """
    Function to plot temperatures for a given month from time_min to time_max

    Args:
        time_min (int): Year to plot from
        time_max (int): Year to plot to
        temp_min (float): Temperature to plot from
        temp_max (float): Temperature to plot to
        month (list): List of months (str)

    Returns:
        figs (list): list of pyplot figures

    """

    temperature_data = pd.read_csv(data,
                                delimiter=',',
                                dtype=float)

    min = int(time_min - temperature_data[['Year']].head(1).values)
    max = int(time_max - temperature_data[['Year']].head(1).values) + 1

    figs = []

    for m in months:
        fig = plt.figure()
        plt.title(f'Temperature in {m} from {time_min} to {time_max}')
        if temp_min:
            plt.ylim(temp_min, temp_max)
        plt.plot(temperature_data['Year'][min:max], temperature_data[m][min:max])
        plt.xlabel('Time [Yr]')
        plt.ylabel('Temperature [$\\mathrm{C^o}$]')

        figs.append(fig)

    return figs



def plot_CO2(data, time_min, time_max, y_min=None, y_max=None):
    """
    Function to plot CO2 concentration from time_min to time_max

    Args:
        data (pandas datafram): Dataframe containing data values in shape 'Year', 'Carbon ppm'
        time_min (int): Year to plot from
        time_max (int): Year to plot to
        y_min (float): ppm to plot from
        y_max (float): ppm to plot to

    Returns:
        Figure: plt.figure

    """

    CO2_data = pd.read_csv(data,
                        delimiter=',',
                        dtype=float)

    min = int(time_min - CO2_data[['Year']].head(1).values)
    max = int(time_max - CO2_data[['Year']].head(1).values) + 1

    fig = plt.figure()

    plt.title(f'$\\mathrm{{CO_2}}$ Concentration from {time_min} to {time_max}')
    plt.plot(CO2_data['Year'][min:max], CO2_data['Carbon'][min:max])
    plt.xlabel('Time [Yr]')
    plt.ylabel('$\\mathrm{CO_2}$ [ppm]')

    return fig


def parse_arguments():
    """
    Collected argparse here
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("time_min",
                        type=int,
                        help="lower bound for time axis")
    parser.add_argument("time_max",
                        type=int,
                        help="upper bound for time axis")
    parser.add_argument("temp_min",
                        type=float,
                        help="lower bound for temp axis")
    parser.add_argument("temp_max",
                        type=float,
                        help="upper bound for temp axis")
    parser.add_argument("months",
                        type=str,
                        nargs='+',
                        help="List of months to plot for")
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_arguments()
    temperature_plots = plot_temperature('./data/temperature.csv', args.time_min, args.time_max, args.months)
    co2_plot = plot_CO2('./data/co2.csv', args.time_min, args.time_max)
    plt.show()
    #fig = plot_CO2(args.CO2_csv, 1880, 2010)
