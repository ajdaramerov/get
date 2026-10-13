import time
import RPi.GPIO as gpio
import r2r_adc
import adc_plot

adc = r2r_adc.R2R_ADC(3.3, compare_time=0.0001, verbose=True)
voltage_values = []
time_values = []
duration = 10.0

try:
    t_start = time.time()
    while (time.time() < duration-t_start):
        voltage_values.add(adc.get_sc_voltage())
        time_values.add(time.time()-t_start)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.3)
finally:
    adc.deinit()
