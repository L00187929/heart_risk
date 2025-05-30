from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model/heart_model.pkl')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from request
        data = request.get_json()

        # Define expected input features in order
        expected_features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                             'restecg', 'thalach', 'exang', 'oldpeak',
                             'slope', 'ca', 'thal']

        # Convert input to numpy array
        input_data = [data[feature] for feature in expected_features]
        input_array = np.array(input_data).reshape(1, -1)

        # Predict using the model
        prediction = model.predict(input_array)[0]

        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"}), 200


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

