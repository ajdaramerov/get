import time
import numpy as np
import RPi.GPIO as gpio

import mcp3021_driver

mcp = mcp3021_driver.MCP3021(dynamic_range=5.0, verbose=False)

times = []
voltages = []

start_time = time.time()

try:
    while time.time() - start_time < 10.0:
        t = time.time()-start_time
        v = mcp.get_voltage()

        times.append(t)
        voltages.append(v)

        print(f"Время: {t:.4f} с, Напряжение: {v:.4f} В")

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Сбор данных остановлен")
finally:
    mcp.deinit()

data = np.column_stack((times, voltages))

np.savetxt("data.csv", data, delimiter=",", fmt="%.4f", header="Время[с],Напряжение[В]",encoding="utf-8")