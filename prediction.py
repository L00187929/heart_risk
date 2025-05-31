import pickle
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model/heart_model.pkl')

# Load model once at import
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

def make_prediction(input_features):
    """
    input_features: list or array of shape (13,)
    Returns: 0 (No heart disease) or 1 (Risk of heart disease)
    """
    input_array = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_array)
    return int(prediction[0])


