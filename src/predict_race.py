import joblib
import pandas as pd

model = joblib.load("models/f1_model.pkl")

def predict_qualifying(drivers, circuit):

    rows = []

    for d in drivers:
        rows.append({
            "Driver": d,
            "Team": "Unknown",
            "Circuit": circuit,
            "AvgSpeed": 200,
            "MaxSpeed": 320
        })

    df = pd.DataFrame(rows)

    df = pd.get_dummies(df)

    predictions = model.predict(df)

    df["PredictedLap"] = predictions

    return df.sort_values("PredictedLap")