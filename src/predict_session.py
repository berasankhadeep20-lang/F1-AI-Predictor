import joblib
import pandas as pd

def predict_knockout(data):

    model = joblib.load("models/f1_model.pkl")

    preds = model.predict(data)

    data["PredictedLap"] = preds

    data = data.sort_values("PredictedLap")

    print("\nProjected Qualifying Order\n")

    print(data[["Driver", "PredictedLap"]])

    print("\nProjected Q1 Knockouts\n")

    print(data.tail(5)["Driver"])