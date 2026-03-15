import joblib
import os

def predict_driver_lap(lap):
    """
    Predict qualifying lap time using telemetry
    """

    # get project root
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # model path
    model_path = os.path.join(base_dir, "models", "f1_model.pkl")

    # load model
    model = joblib.load(model_path)

    # telemetry
    tel = lap.get_car_data()

    avg_speed = tel["Speed"].mean()
    max_speed = tel["Speed"].max()

    X = [[avg_speed, max_speed]]

    prediction = model.predict(X)[0]

    return prediction