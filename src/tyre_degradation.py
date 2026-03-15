import fastf1
import matplotlib.pyplot as plt
import pandas as pd

fastf1.Cache.enable_cache("cache")

def tyre_degradation(year, race):

    print("Loading race data...")

    session = fastf1.get_session(year, race, "R")
    session.load()

    laps = session.laps.pick_quicklaps()

    drivers = laps["Driver"].unique()

    plt.figure(figsize=(10,6))

    for driver in drivers:

        driver_laps = laps.pick_driver(driver)

        lap_times = driver_laps["LapTime"].dt.total_seconds()

        plt.plot(lap_times, label=driver)

    plt.title(f"Tyre Degradation - {race}")
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")

    plt.legend()

    plt.show()


if __name__ == "__main__":

    tyre_degradation(2024, "Bahrain Grand Prix")

import fastf1
import matplotlib.pyplot as plt
import pandas as pd

fastf1.Cache.enable_cache("cache")

def tyre_degradation(year, race):

    print("Loading race data...")

    session = fastf1.get_session(year, race, "R")
    session.load()

    laps = session.laps.pick_quicklaps()

    drivers = laps["Driver"].unique()

    plt.figure(figsize=(10,6))

    for driver in drivers:

        driver_laps = laps.pick_driver(driver)

        lap_times = driver_laps["LapTime"].dt.total_seconds()

        plt.plot(lap_times, label=driver)

    plt.title(f"Tyre Degradation - {race}")
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")

    plt.legend()

    plt.show()


if __name__ == "__main__":

    tyre_degradation(2024, "Bahrain Grand Prix")