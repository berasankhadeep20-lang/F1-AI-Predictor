import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "f1_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_2026_grid(drivers, circuit):

    rows = []

    for driver in drivers:

        rows.append({
            "Driver": driver,
            "Team": "Unknown",
            "Circuit": circuit,
            "AvgSpeed": 210,
            "MaxSpeed": 325
        })

    df = pd.DataFrame(rows)

    # encode like training
    df = pd.get_dummies(df)

    predictions = model.predict(df)

    df["PredictedLap"] = predictions

    return df.sort_values("PredictedLap")