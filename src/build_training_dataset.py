import fastf1
import pandas as pd

fastf1.Cache.enable_cache("cache")

seasons = [2023, 2024]

rows = []

for year in seasons:

    schedule = fastf1.get_event_schedule(year)

    for rnd in schedule['RoundNumber']:

        try:
            session = fastf1.get_session(year, rnd, 'Q')
            session.load()

            laps = session.laps.pick_fastest()

            for _, lap in laps.iterlaps():

                tel = lap.get_car_data()

                avg_speed = tel['Speed'].mean()
                max_speed = tel['Speed'].max()

                rows.append({
                    "Driver": lap['Driver'],
                    "Team": lap['Team'],
                    "Circuit": session.event['EventName'],
                    "AvgSpeed": avg_speed,
                    "MaxSpeed": max_speed,
                    "LapTime": lap['LapTime'].total_seconds()
                })

        except:
            continue

df = pd.DataFrame(rows)

df.to_csv("data/f1_training_data.csv", index=False)

print("Dataset created")