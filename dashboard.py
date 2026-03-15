import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import fastf1
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os

# ------------------------------
# FASTF1 CACHE
# ------------------------------

fastf1.Cache.enable_cache("cache")

# ------------------------------
# PAGE CONFIG
# ------------------------------

st.set_page_config(
    page_title="F1 AI Analytics",
    layout="wide"
)

st.title("🏎 Formula 1 AI Analytics Dashboard")

# ------------------------------
# LOAD AI MODEL
# ------------------------------

model = None
model_path = "models/f1_model.pkl"

if os.path.exists(model_path):
    try:
        model = joblib.load(model_path)
    except:
        st.warning("AI model could not be loaded.")

# ------------------------------
# FASTF1 SESSION LOADER
# ------------------------------

@st.cache_data(show_spinner=False)
def load_session(year, event, session_type):
    session = fastf1.get_session(year, event, session_type)
    session.load()
    return session

# ------------------------------
# SIDEBAR SETTINGS
# ------------------------------

st.sidebar.header("Session Controls")

year = st.sidebar.selectbox(
    "Season",
    [2023, 2024, 2025]
)

schedule = fastf1.get_event_schedule(year)

event = st.sidebar.selectbox(
    "Grand Prix",
    schedule["EventName"].tolist()
)

session_type = st.sidebar.selectbox(
    "Session",
    ["FP1", "FP2", "FP3", "Q", "R"]
)

# ------------------------------
# LOAD SESSION
# ------------------------------

st.subheader("Session Data")

try:
    session = load_session(year, event, session_type)
except:
    st.error("Session data not available.")
    st.stop()

st.success(f"{event} {session_type} loaded")

# ------------------------------
# DRIVER SELECTION
# ------------------------------

drivers = sorted(session.laps["Driver"].dropna().unique())

driver = st.sidebar.selectbox(
    "Driver",
    drivers
)

driver_laps = session.laps.pick_drivers(driver)

if driver_laps.empty:
    st.warning("No laps available for this driver.")
    st.stop()

fastest_lap = driver_laps.pick_fastest()

# ------------------------------
# SPEED TELEMETRY GRAPH
# ------------------------------

st.subheader("Speed Trace")

try:
    tel = fastest_lap.get_car_data().add_distance()

    fig, ax = plt.subplots()

    ax.plot(
        tel["Distance"],
        tel["Speed"]
    )

    ax.set_xlabel("Distance")
    ax.set_ylabel("Speed")
    ax.set_title(f"{driver} Fastest Lap Speed")

    st.pyplot(fig)

except:
    st.warning("Telemetry unavailable for this lap.")

# ------------------------------
# LAP TIMES TABLE
# ------------------------------

st.subheader("Lap Times")

lap_table = driver_laps[[
    "LapNumber",
    "LapTime",
    "Compound"
]].dropna()

st.dataframe(lap_table)

# ------------------------------
# DRIVER COMPARISON GRAPH
# ------------------------------

st.subheader("Driver Lap Comparison")

compare_drivers = st.multiselect(
    "Select drivers to compare",
    drivers,
    default=drivers[:3]
)

fig2, ax2 = plt.subplots()

for d in compare_drivers:

    laps = session.laps.pick_drivers(d)

    if laps.empty:
        continue

    lap_times = laps["LapTime"].dropna().dt.total_seconds()

    ax2.plot(
        lap_times.values,
        label=d
    )

ax2.set_xlabel("Lap Index")
ax2.set_ylabel("Lap Time (seconds)")
ax2.legend()

st.pyplot(fig2)

# ------------------------------
# AI QUALIFYING PREDICTION
# ------------------------------

st.subheader("AI Qualifying Prediction")

if model is None:

    st.info("AI model not found. Train the model first.")

else:

    try:

        avg_lap = driver_laps["LapTime"].dropna().mean().total_seconds()
        grid_pos = 10

        X = pd.DataFrame(
            [[avg_lap, grid_pos]],
            columns=[
                "avg_lap_time",
                "grid_position"
            ]
        )

        prediction = model.predict(X)[0]

        st.metric(
            label="Predicted Qualifying Lap Time",
            value=f"{prediction:.3f} seconds"
        )

    except:
        st.warning("Prediction could not be generated.")

# ------------------------------
# SESSION SUMMARY
# ------------------------------

st.subheader("Session Summary")

st.write("Drivers:", len(drivers))
st.write("Total Laps:", len(session.laps))