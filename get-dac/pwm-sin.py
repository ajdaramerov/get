import pwm_dac as pd
import signal_generator as sg 

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    gpio_pin = 12
    dac = pd.PWM_DAC(gpio_pin, pwm_frequency, dynamic_range=3.3)

    t = 0.0

    while True:
        normalized_value = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = normalized_value*amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t += 1.0 / sampling_frequency

except KeyboardInterrupt:
    print("\nГенерация остановлена пользователем.")
finally:
    dac.deinit()