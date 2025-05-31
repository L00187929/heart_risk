import unittest
import json
from flaskapp import app  # Import your Flask app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_status(self):
        # Test GET /status
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('status', data)
        self.assertEqual(data['status'], 'OK')

    def test_predict_valid_input(self):
        # Prepare a valid input dictionary with expected features
        valid_input = {
            "age": 63,
            "sex": 1,
            "cp": 3,
            "trestbps": 145,
            "chol": 233,
            "fbs": 1,
            "restecg": 0,
            "thalach": 150,
            "exang": 0,
            "oldpeak": 2.3,
            "slope": 0,
            "ca": 0,
            "thal": 1
        }
        response = self.app.post('/predict', data=json.dumps(valid_input), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('prediction', data)
        self.assertIn(data['prediction'], [0, 1])  # Prediction should be 0 or 1

    def test_predict_missing_feature(self):
        # Missing one required feature 'chol'
        invalid_input = {
            "age": 63,
            "sex": 1,
            "cp": 3,
            "trestbps": 145,
            # "chol": 233,  # missing on purpose
            "fbs": 1,
            "restecg": 0,
            "thalach": 150,
            "exang": 0,
            "oldpeak": 2.3,
            "slope": 0,
            "ca": 0,
            "thal": 1
        }
        response = self.app.post('/predict', data=json.dumps(invalid_input), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
