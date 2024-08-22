from flask import Flask, request, jsonify
import joblib
import numpy as np
import base64
from PIL import Image
import io

app = Flask(__name__)

# Carregar o modelo treinado
model = joblib.load("models/model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    img_data = base64.b64decode(data['image'])
    img = Image.open(io.BytesIO(img_data)).convert('L')
    img = img.resize((8, 8))
    img_array = np.array(img).reshape(1, -1)
    prediction = model.predict(img_array)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
