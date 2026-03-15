import fastf1
import fastf1.utils
import matplotlib.pyplot as plt
import logging

# -------------------------
# Disable FastF1 logs
# -------------------------
logging.getLogger("fastf1").setLevel(logging.ERROR)

# -------------------------
# Enable cache
# -------------------------
fastf1.Cache.enable_cache("cache")

# -------------------------
# Driver colors
# -------------------------
driver_colors = {
    "VER": "#0600EF",
    "PER": "#0600EF",
    "LEC": "#DC0000",
    "SAI": "#DC0000",
    "HAM": "#00D2BE",
    "RUS": "#00D2BE",
    "NOR": "#FF8700",
    "PIA": "#FF8700",
    "ALO": "#006F62",
    "STR": "#006F62",
    "OCO": "#0090FF",
    "GAS": "#0090FF",
    "ALB": "#005AFF",
    "SAR": "#005AFF",
    "TSU": "#2B4562",
    "RIC": "#2B4562",
    "BOT": "#900000",
    "ZHO": "#900000",
    "MAG": "#B6BABD",
    "HUL": "#B6BABD"
}


def lap_delta_all_drivers(year, race):

    print(f"\nLoading {race} Qualifying...\n")

    session = fastf1.get_session(year, race, "Q")
    session.load()

    laps = session.laps.pick_quicklaps()

    reference_lap = laps.pick_fastest()
    reference_driver = reference_lap["Driver"]

    print("Reference Driver:", reference_driver)

    ref_tel = reference_lap.get_car_data().add_distance()

    drivers = sorted(laps["Driver"].unique())

    track_length = ref_tel["Distance"].max()

    sector1 = track_length / 3
    sector2 = 2 * track_length / 3

    plt.figure(figsize=(14,8))

    # sector shading
    plt.axvspan(0, sector1, alpha=0.05)
    plt.axvspan(sector1, sector2, alpha=0.08)
    plt.axvspan(sector2, track_length, alpha=0.05)

    for driver in drivers:

        try:

            lap = laps.pick_drivers(driver).pick_fastest()

            delta_time, ref_tel, compare_tel = fastf1.utils.delta_time(
                reference_lap,
                lap
            )

            color = driver_colors.get(driver, "gray")

            plt.plot(
                ref_tel["Distance"],
                delta_time,
                label=driver,
                color=color,
                linewidth=2
            )

        except Exception as e:
            print(f"Skipping {driver}: {e}")

    plt.axhline(0, linestyle="--")

    plt.title(f"{race} Qualifying Lap Delta vs {reference_driver}")

    plt.xlabel("Track Distance (meters)")
    plt.ylabel("Time Delta (seconds)")

    plt.legend(
        bbox_to_anchor=(1.02,1),
        loc="upper left",
        fontsize=8
    )

    plt.tight_layout()

    plt.show()


# -------------------------
# MAIN PROGRAM
# -------------------------
if __name__ == "__main__":

    year = 2024

    # load race schedule
    schedule = fastf1.get_event_schedule(year)

    races = schedule["EventName"].tolist()

    print("\nAvailable Grand Prix:\n")

    for i, race in enumerate(races):
        print(f"{i+1}. {race}")

    choice = int(input("\nSelect race number: "))

    race = races[choice-1]

    lap_delta_all_drivers(year, race)