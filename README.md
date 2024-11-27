
# DIABETES RISK PREDICTOR

## Description
This is a Diabetes Risk Prediction Tool designed to help both healthcare professionals and individuals assess the risk of diabetes through a simple web interface. The tool uses machine learning to analyze various health metrics such as blood pressure, BMI, glucose levels, and other clinical indicators to provide quick and reliable predictions.

Note: This tool is intended for screening purposes only and should not be used as a substitute for professional medical diagnosis or advice.


## Dependencies

1. Install Python 3.x
2. Install required packages:
   - Flask
   - pandas
   - scikit-learn
   - joblib
   - flask-cors

   Use command: pip install flask pandas scikit-learn joblib flask-cors

    or

    Simply use this command: pip install -r requirements.txt

## API Usage

Endpoint: POST /api/predict

Sample Request:
{
    "Pregnancy": 0,
    "Plasma": 100,
    "BloodPressure": 70,
    "Skin": 30,
    "Test": 80,
    "BMI": 25,
    "DBF": 0.5,
    "Age": 30
}

Response:
{
    "risk_score": "Diabetic" or "Non Diabetic"
}

Static Files:
------------
- Homepage: GET /
- Other static files: GET /<path


Running the Application:
----------------------
1. Navigate to the project directory
2. Run: python src/main.py
3. Access the application at http://localhost:5000
## Demo




![Recording2024-11-27164326-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/1d727adb-5939-40a2-acb3-be1f6c659ea4)
## Results

Image 1: - Website

![Result 1](https://github.com/user-attachments/assets/4c635c65-31cd-4e1e-945a-c26ccbe95f3a)


Image 2:- Diabetic Prediction

![Result 2](https://github.com/user-attachments/assets/440e35b1-ed9c-4662-a178-f6bb0911990a)

Image 3:- Non - Diabetic Prediction

![Result 3](https://github.com/user-attachments/assets/e509be4a-7a9e-4582-9f09-b441efd515d4)
