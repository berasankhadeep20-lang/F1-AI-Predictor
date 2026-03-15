import joblib
import pandas as pd

model = joblib.load("../models/qualifying_model.pkl")

data = pd.read_csv("../data/new_session.csv")

predictions = model.predict(data)

print(predictions)