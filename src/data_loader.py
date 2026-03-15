import fastf1
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CACHE_DIR = os.path.join(BASE_DIR, "cache")

os.makedirs(CACHE_DIR, exist_ok=True)

fastf1.Cache.enable_cache(CACHE_DIR)

def load_season(year):

    races = fastf1.get_event_schedule(year)

    all_laps = []

    for race in races['EventName']:

        try:
            session = fastf1.get_session(year, race, 'Q')
            session.load()

            laps = session.laps[['Driver','LapTime','Sector1Time','Sector2Time','Sector3Time','Compound']]
            laps.loc[:, "Race"] = race
            laps.loc[:, "Year"] = year

            all_laps.append(laps)

        except:
            print(f"Skipped {race}")

    df = pd.concat(all_laps)
    return df