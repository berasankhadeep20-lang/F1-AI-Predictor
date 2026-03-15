import os
import sys

print("\n===================================")
print("        F1 AI Predictor")
print("===================================\n")

print("Starting full analytics pipeline...\n")


# ===============================
# STEP 1 - DOWNLOAD DATA
# ===============================

print("Step 1: Downloading telemetry data...\n")

os.system("python src/download_data.py")


# ===============================
# STEP 2 - PROCESS DATA
# ===============================

print("\nStep 2: Processing dataset...\n")

os.system("python src/process_data.py")


# ===============================
# STEP 3 - TRAIN MODEL
# ===============================

print("\nStep 3: Training machine learning model...\n")

os.system("python src/train_model.py")


# ===============================
# STEP 4 - PREDICT QUALIFYING
# ===============================

print("\nStep 4: Predicting qualifying results...\n")

os.system("python src/predict_session.py")


# ===============================
# STEP 5 - DRIVER PACE ANALYSIS
# ===============================

print("\nStep 5: Driver race pace analysis...\n")

os.system("python src/driver_pace.py")


# ===============================
# STEP 6 - TELEMETRY COMPARISON
# ===============================

print("\nStep 6: Telemetry comparison...\n")

os.system("python src/telemetry_analysis.py")


# ===============================
# STEP 7 - TYRE DEGRADATION
# ===============================

print("\nStep 7: Tyre degradation analysis...\n")

os.system("python src/tyre_degradation.py")


print("\n===================================")
print("   F1 AI Pipeline Completed")
print("===================================\n")