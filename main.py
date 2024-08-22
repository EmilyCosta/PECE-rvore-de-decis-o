from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Carregar o modelo treinado (assumindo que você o salvou como 'model.joblib')
model = joblib.load("model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict(np.array(data['input']).reshape(1, -1))
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
