import streamlit as st
import joblib
import numpy as np
import os

st.title("Diabetes Progression Predictor")

# Load model with path relative to this script
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model.pkl")
model = joblib.load(model_path)

st.subheader("Enter Patient Features")

age = st.number_input("Age", min_value=0)
sex_str = st.selectbox("Sex", options=["Female", "Male"])
sex = 1 if sex_str == "Male" else 0
bmi = st.number_input("Body Mass Index (BMI)")
bp = st.number_input("Average Blood Pressure")
s1 = st.number_input("Total Cholesterol (S1)")
s2 = st.number_input("LDL Cholesterol (S2)")
s3 = st.number_input("HDL Cholesterol (S3)")
s4 = st.number_input("Total Cholesterol / HDL Ratio (S4)")
s5 = st.number_input("Log of Serum Triglycerides (S5)")
s6 = st.number_input("Glucose Serum Level (S6)")

if st.button("Predict Progression"):
    try:
        features = [float(age), float(sex), float(bmi), float(bp),
                    float(s1), float(s2), float(s3), float(s4), float(s5), float(s6)]
        features = np.array(features).reshape(1, -1)
        prediction = model.predict(features)
        st.success(f"Predicted Disease Progression: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Invalid input: {e}")
