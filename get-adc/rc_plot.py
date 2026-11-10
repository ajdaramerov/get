import numpy as np

from adc_plot import plot_voltage_vs_time

filename = 'data.csv'

data = np.loadtxt(filename, delimiter=",", skiprows=1)

times = data[:, 0].tolist()
voltages = data[:, 1].tolist()

plot_voltage_vs_time(times, voltages, max_voltage=max(voltages), filename="rc-plot.png")
