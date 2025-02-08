import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# Set page configuration with dark theme
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #262730;
        color: #FAFAFA;
        border: 1px solid #4B4B4B;
    }
    .stButton>button:hover {
        background-color: #363940;
        color: #FFFFFF;
        border: 1px solid #565656;
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: #FAFAFA;
    }
    .stNumberInput>div>div>input {
        background-color: #262730;
        color: #FAFAFA;
    }
    .stSelectbox>div>div {
        background-color: #262730;
        color: #FAFAFA;
    }
    .stHeader {
        background-color: transparent;
    }
    .stMarkdown {
        color: #FAFAFA;
    }
    .stExpander {
        background-color: #262730;
    }
    .stProgress .st-bo {
        background-color: #4CAF50;
    }
    div[data-baseweb="select"] {
        background-color: #262730;
    }
    div[role="listbox"] ul {
        background-color: #262730;
    }
    div[data-baseweb="select"] * {
        background-color: #262730;
    }
    .stSlider>div>div {
        background-color: #4B4B4B;
    }
    .stSlider>div>div>div>div {
        background-color: #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Load the full model pipeline (preprocessor + model)
@st.cache_resource
def load_model():
    try:
        return joblib.load("model.pkl")  # This returns (preprocessor, model)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

preprocessor, model = load_model()

# Function to make predictions
def predict_diabetes(inputs):
    input_df = pd.DataFrame([inputs])  # Convert input to DataFrame
    try:
        input_transformed = preprocessor.transform(input_df)  # Apply preprocessing
        prediction = model.predict(input_transformed)  # Make prediction
        probability = model.predict_proba(input_transformed)[0][1]  # Get probability of positive class
        return prediction[0], probability
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None, None

# Streamlit UI
st.title("🩺 Diabetes Prediction App")
st.write("This app predicts the likelihood of diabetes based on various health factors.")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    st.subheader("Personal Information")
    gender = st.selectbox("Gender", ["male", "female", "other"])
    age = st.slider("Age", 0, 80, 25)
    bmi = st.number_input("BMI", min_value=10.16, max_value=71.55, value=25.0, format="%.2f")
    
with col2:
    st.subheader("Medical Information")
    hypertension = st.selectbox("Hypertension", ["No", "Yes"])
    heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
    smoking_history = st.selectbox("Smoking History", ["not current", "former", "No Info", "current", "never", "ever"])
    HbA1c_level = st.number_input("HbA1c Level", min_value=0.0, value=5.7, format="%.1f")
    blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0.0, value=100.0, format="%.1f")

# Convert categorical values
inputs = {
    "gender": gender,
    "age": age,
    "hypertension": 1 if hypertension == "Yes" else 0,
    "heart_disease": 1 if heart_disease == "Yes" else 0,
    "smoking_history": smoking_history,
    "bmi": bmi,
    "HbA1c_level": HbA1c_level,
    "blood_glucose_level": blood_glucose_level
}

if st.button("Predict Diabetes", key="predict"):
    if model:
        with st.spinner("Analyzing your data..."):
            result, probability = predict_diabetes(inputs)
        if result is not None:
            st.subheader("Prediction Result")
            if result == 1:
                st.error("⚠️ The person is likely to be diabetic.")
            else:
                st.success("✅ The person is likely to be non-diabetic.")
            
            # Create a gauge chart for the probability
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = probability * 100,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Probability of Diabetes"},
                gauge = {
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "darkblue"},
                    'steps' : [
                        {'range': [0, 33], 'color': "lightgreen"},
                        {'range': [33, 66], 'color': "yellow"},
                        {'range': [66, 100], 'color': "red"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': probability * 100
                    }
                }
            ))
            st.plotly_chart(fig)

            st.write(f"The model predicts a {probability:.2%} chance of diabetes.")
            
            # Display recommendations based on the prediction
            st.subheader("Recommendations")
            if result == 1:
                st.warning("""
                - Consult with a healthcare professional for a thorough evaluation.
                - Monitor your blood glucose levels regularly.
                - Maintain a healthy diet and exercise routine.
                - Consider lifestyle changes to manage your risk factors.
                """)
            else:
                st.info("""
                - Continue maintaining a healthy lifestyle.
                - Regular check-ups are still important for early detection.
                - Stay informed about diabetes risk factors and symptoms.
                """)
    else:
        st.error("Model is not loaded properly.")

# Add an explanation section
with st.expander("How does this prediction work?"):
    st.write("""
    This diabetes prediction model uses machine learning to analyze various health factors and estimate the likelihood of diabetes. Here's a brief explanation of the input factors:

    - **Gender**: Biological sex can influence diabetes risk.
    - **Age**: Risk of type 2 diabetes increases with age.
    - **BMI (Body Mass Index)**: A higher BMI is associated with increased diabetes risk.
    - **Hypertension**: High blood pressure is often associated with diabetes.
    - **Heart Disease**: Cardiovascular issues can be linked to diabetes.
    - **Smoking History**: Smoking can affect insulin sensitivity and increase diabetes risk.
    - **HbA1c Level**: This test reflects average blood sugar levels over the past 2-3 months.
    - **Blood Glucose Level**: High blood sugar is a key indicator of diabetes.

    Remember, this tool provides an estimate based on the information given and should not be considered a medical diagnosis. Always consult with healthcare professionals for proper medical advice and diagnosis.
    """)


