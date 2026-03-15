import pandas as pd

def prepare_features(file):

    df = pd.read_csv(file)

    df['LapTime'] = pd.to_timedelta(df['LapTime']).dt.total_seconds()
    df['Sector1Time'] = pd.to_timedelta(df['Sector1Time']).dt.total_seconds()
    df['Sector2Time'] = pd.to_timedelta(df['Sector2Time']).dt.total_seconds()
    df['Sector3Time'] = pd.to_timedelta(df['Sector3Time']).dt.total_seconds()

    df = df.dropna()

    return df