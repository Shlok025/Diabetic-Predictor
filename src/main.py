from flask import Flask, request, jsonify, send_from_directory
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__, static_folder='../static')
CORS(app)
model = joblib.load('src/model_joblib')

@app.route('/')
def serve_static():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = pd.DataFrame([{
        'Pregnancy': data['Pregnancy'],
        'Plasma': data['Plasma'],
        'BloodPressure': data['BloodPressure'],
        'Skin': data['Skin'],
        'Test': data['Test'],
        'BMI': data['BMI'],
        'DBF': data['DBF'],
        'Age': data['Age']
    }])
    prediction = model.predict(input_data)
    
    # Map prediction to terms
    risk_term = "Diabetic" if prediction[0] == 1 else "Non Diabetic"
    
    return jsonify({'risk_score': risk_term})

if __name__ == '__main__':
    app.run(debug=True )
