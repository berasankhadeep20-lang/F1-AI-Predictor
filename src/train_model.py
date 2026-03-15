import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# =========================
# PATH CONFIG
# =========================

DATA_PATH = "data/processed/dataset.csv"
MODEL_DIR = "models"
MODEL_PATH = f"{MODEL_DIR}/f1_model.pkl"

os.makedirs(MODEL_DIR, exist_ok=True)


# =========================
# LOAD DATA
# =========================

def load_dataset():

    print("Loading dataset...")

    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:", df.shape)

    return df


# =========================
# TRAIN MODEL
# =========================

def train_model():

    df = load_dataset()

    # Features used for training
    features = [

        "Sector1Time",
        "Sector2Time",
        "Sector3Time",
        "Compound",
        "TyreLife",
        "Driver",
        "Team",
        "Race",
        "TrackTemp",
        "AirTemp",
        "Humidity",
        "WindSpeed"

    ]

    X = df[features]
    y = df["LapTime"]

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # =========================
    # MODEL
    # =========================

    print("Training RandomForest model...")

    model = RandomForestRegressor(
        n_estimators=300,
        random_state=42
    )

    model.fit(X_train, y_train)

    # =========================
    # PREDICTIONS
    # =========================

    preds = model.predict(X_test)

    # =========================
    # METRICS
    # =========================

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print("\nModel Evaluation")
    print("----------------")
    print("MAE:", mae, "seconds")
    print("R2 Score:", r2)

    # =========================
    # SAVE MODEL
    # =========================

    joblib.dump(model, MODEL_PATH)

    print("\nModel saved to:", MODEL_PATH)

    # =========================
    # GRAPH 1
    # Predicted vs Actual
    # =========================

    plt.figure(figsize=(8,6))

    plt.scatter(y_test, preds)

    plt.xlabel("Actual Lap Time (s)")
    plt.ylabel("Predicted Lap Time (s)")
    plt.title("Predicted vs Actual Lap Times")

    # perfect prediction line
    plt.plot(
        [min(y_test), max(y_test)],
        [min(y_test), max(y_test)]
    )

    plt.show()

    # =========================
    # GRAPH 2
    # Error Distribution
    # =========================

    errors = y_test - preds

    plt.figure(figsize=(8,6))

    plt.hist(errors, bins=40)

    plt.title("Prediction Error Distribution")
    plt.xlabel("Prediction Error (seconds)")
    plt.ylabel("Frequency")

    plt.show()

    # =========================
    # GRAPH 3
    # Feature Importance
    # =========================

    importance = model.feature_importances_

    imp_df = pd.DataFrame({
        "Feature": X.columns,
        "Importance": importance
    })

    imp_df = imp_df.sort_values("Importance")

    plt.figure(figsize=(8,6))

    plt.barh(imp_df["Feature"], imp_df["Importance"])

    plt.title("Feature Importance")

    plt.show()

    # =========================
    # GRAPH 4
    # Sorted comparison
    # =========================

    comparison = pd.DataFrame({
        "Actual": y_test,
        "Predicted": preds
    })

    comparison = comparison.sort_values("Actual")

    comparison.plot(figsize=(10,6))

    plt.title("Actual vs Predicted Lap Times")

    plt.show()

import fastf1
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

fastf1.Cache.enable_cache("cache")

def build_dataset(year):

    schedule = fastf1.get_event_schedule(year)

    rows = []

    for race in schedule["EventName"]:

        try:
            session = fastf1.get_session(year, race, "Q")
            session.load()

            laps = session.laps.pick_quicklaps()

            for _, lap in laps.iterrows():

                tel = lap.get_car_data()

                avg_speed = tel["Speed"].mean()
                max_speed = tel["Speed"].max()

                rows.append({
                    "driver": lap["Driver"],
                    "avg_speed": avg_speed,
                    "max_speed": max_speed,
                    "lap_time": lap["LapTime"].total_seconds()
                })

        except:
            continue

    return pd.DataFrame(rows)


data = build_dataset(2024)

X = data[["avg_speed", "max_speed"]]
y = data["lap_time"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "model.pkl")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("data/f1_training_data.csv")

# encode categorical
df = pd.get_dummies(df, columns=["Driver","Team","Circuit"])

X = df.drop("LapTime", axis=1)
y = df["LapTime"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=200)

model.fit(X_train, y_train)

joblib.dump(model, "models/f1_model.pkl")

print("Model trained and saved")

# =========================
# MAIN
# =========================

if __name__ == "__main__":

    train_model()
