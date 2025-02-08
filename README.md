# Diabetes Prediction App

## Overview

*Diabetes Prediction App* is an interactive **Streamlit-based** application that predicts whether a person is diabetic or not based on several health factors. The app leverages **machine learning** models trained on relevant health data to provide accurate predictions. Users can enter their details, and the model will analyze the input to determine the likelihood of diabetes.

## Features

### Key Features
- **Machine Learning-Based Predictions**: Uses a trained **RandomForestClassifier** for accurate results.
- **Interactive UI**: Built using **Streamlit** with a **dark-themed UI** for an enhanced experience.
- **Health Factors Considered**: Inputs include gender, age, BMI, hypertension, heart disease, smoking history, HbA1c level, and blood glucose level.
- **Probability Gauge**: Displays the probability of diabetes using **Plotly** gauge charts.
- **Recommendations**: Provides health suggestions based on the prediction result.
- **Expandable Explanations**: Users can explore detailed descriptions of how each factor contributes to the prediction.

### Visualizations and UI Components
1. **User Input Fields**: Users can enter their health details via dropdowns, sliders, and number inputs.
2. **Prediction Output**: Displays whether the person is likely to be diabetic or not.
3. **Probability Gauge Chart**: Shows the likelihood of diabetes using **Plotly Gauge Indicators**.
4. **Health Recommendations**: Personalized tips based on the model's prediction.

## Requirements

To run this app, ensure the following dependencies are installed:

1. *Streamlit*: For building the interactive UI.
2. *Pandas*: Required for handling data structures.
3. *Joblib*: To load the trained machine learning model.
4. *Plotly*: Used for generating interactive probability visualizations.
5. *Scikit-learn*: Required for the machine learning model.

Install the dependencies using:

```bash
pip install streamlit pandas joblib plotly scikit-learn
```

## Setup Instructions

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Shlok025/Diabetes-Prediction-App.git
cd Diabetes-Prediction-App
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

## Usage

1. Launch the app in your browser.
2. Enter personal and medical details like **age, gender, BMI, hypertension status, and blood glucose level**.
3. Click **"Predict Diabetes"** to generate a prediction.
4. View the **prediction result, probability gauge, and health recommendations**.
5. Expand the **"How does this prediction work?"** section to learn more about the model.

## Images

### **App UI:**
![Home](https://github.com/user-attachments/assets/51f4c886-8690-43d6-97d0-4f914bea5b12)

### **Prediction & Probability Gauge:**
![Probability Gauge](https://github.com/user-attachments/assets/9ffa8eb1-3936-482e-ac53-88d63c92d5ac)

## Contribution

Contributions are welcome! If you have suggestions for improvements or encounter issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Footer

Developed with ❤ by [Shlok Gaikwad](https://github.com/Shlok025/)

⚡ Features: Machine Learning-Based Prediction, Probability Gauge, Interactive UI, and Health Recommendations.

