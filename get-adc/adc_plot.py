import matplotlib as plt

def plot_voltage_vs_time(time, voltage, max_voltage, filename=None):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.xlable("Время,  c")
    plt.ylable("Напряжение, В")
    plt.set_xlim(max(time))
    plt.set_ylim(max_voltage)
    plt.label("Зависимость напряжения от времени")
    plt.gird()

    if filename:
        plt.savefig(filename, dpi=150)
    plt.show()
