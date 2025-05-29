import pickle
import numpy as np
import os

# Load model from the saved pickle file
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model/heart_model.pkl')

def load_model():
    with open(MODEL_PATH, 'rb') as file:
        model = pickle.load(file)
    return model

# Function to predict based on input features
def make_prediction(input_features):
    """
    input_features: list or array of shape (13,)
    Returns: 0 (No heart disease) or 1 (Risk of heart disease)
    """
    model = load_model()
    input_array = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_array)
    return int(prediction[0])

