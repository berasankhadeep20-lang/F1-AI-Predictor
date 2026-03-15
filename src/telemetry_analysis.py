import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache("cache")

def telemetry_compare(year, race, driver1, driver2):

    session = fastf1.get_session(year, race, "Q")
    session.load()

    lap1 = session.laps.pick_driver(driver1).pick_fastest()
    lap2 = session.laps.pick_driver(driver2).pick_fastest()

    tel1 = lap1.get_car_data().add_distance()
    tel2 = lap2.get_car_data().add_distance()

    plt.figure(figsize=(10,6))

    plt.plot(tel1["Distance"], tel1["Speed"], label=driver1)
    plt.plot(tel2["Distance"], tel2["Speed"], label=driver2)

    plt.xlabel("Distance")
    plt.ylabel("Speed (km/h)")

    plt.title("Telemetry Speed Comparison")

    plt.legend()

    plt.show()

if __name__ == "__main__":
    telemetry_compare(2024, "Bahrain Grand Prix", "VER", "LEC")