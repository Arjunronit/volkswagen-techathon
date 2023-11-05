from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load your machine learning model
loaded_model = joblib.load(
    'C:\volkswagen-techathon\ML Models\maintenance_duration_model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_maintenance_duration', methods=['POST'])
def predict_maintenance_duration():
    try:
        # Get input features from the request data
        input_data = request.json

        # Call your machine learning model to predict maintenance duration
        predicted_duration = loaded_model.predict([input_data])

        response = {'predicted_maintenance_duration': predicted_duration[0]}
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
