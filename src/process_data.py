import os
import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder

# ==============================
# PATHS
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(PROCESSED_DIR, "dataset.csv")


# ==============================
# LOAD RAW DATA
# ==============================

def load_raw_data():

    print("Loading raw datasets...")

    files = os.listdir(RAW_DIR)

    dfs = []

    for file in files:

        if file.endswith(".csv"):

            path = os.path.join(RAW_DIR, file)

            print("Reading:", file)

            df = pd.read_csv(path)

            dfs.append(df)

    dataset = pd.concat(dfs, ignore_index=True)

    print("Total rows:", len(dataset))

    return dataset


# ==============================
# PROCESS DATA
# ==============================

def process_dataset():

    df = load_raw_data()

    print("\nProcessing dataset...")

    # Convert lap times to seconds
    df["LapTime"] = pd.to_timedelta(df["LapTime"]).dt.total_seconds()
    df["Sector1Time"] = pd.to_timedelta(df["Sector1Time"]).dt.total_seconds()
    df["Sector2Time"] = pd.to_timedelta(df["Sector2Time"]).dt.total_seconds()
    df["Sector3Time"] = pd.to_timedelta(df["Sector3Time"]).dt.total_seconds()

    # Remove missing values
    df = df.dropna()

    print("Rows after cleaning:", len(df))

    # ==============================
    # ENCODE CATEGORICAL FEATURES
    # ==============================

    encoders = {}

    categorical_cols = ["Driver", "Team", "Compound", "Race"]

    for col in categorical_cols:

        print("Encoding:", col)

        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(df[col])

        encoders[col] = encoder

    # Save encoders
    encoder_path = os.path.join(MODEL_DIR, "encoders.pkl")

    joblib.dump(encoders, encoder_path)

    print("Encoders saved:", encoder_path)

    # ==============================
    # SAVE PROCESSED DATASET
    # ==============================

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nProcessed dataset saved to:")
    print(OUTPUT_FILE)

    print("\nDataset shape:", df.shape)


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":

    process_dataset()