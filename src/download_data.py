import pandas as pd
from data_loader import load_season

print("Downloading seasons...")

df2023 = load_season(2023)
df2024 = load_season(2024)

print("Combining datasets...")

df = pd.concat([df2023, df2024], ignore_index=True)

df.to_csv("data/raw/f1_laps.csv", index=False)

print("Dataset saved to data/raw/f1_laps.csv")