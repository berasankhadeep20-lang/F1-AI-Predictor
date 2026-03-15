import fastf1
import pandas as pd
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache("cache")

def driver_pace(year, race):

    session = fastf1.get_session(year, race, "R")
    session.load()

    laps = session.laps.pick_quicklaps()

    pace = laps.groupby("Driver")["LapTime"].mean()

    pace = pace.sort_values()

    pace_seconds = pace.dt.total_seconds()

    pace_seconds.plot(kind="bar")

    plt.title(f"Driver Race Pace - {race}")
    plt.ylabel("Average Lap Time (s)")

    plt.show()

if __name__ == "__main__":
    driver_pace(2024, "Bahrain Grand Prix")