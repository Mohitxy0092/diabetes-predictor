import streamlit as st
import joblib
import numpy as np

st.title("Diabetes Progression Predictor")

# Load model
model = joblib.load("model.pkl")

st.subheader("Enter Patient Details")

# Create 10 separate input fields
age = st.number_input("Age")
sex = st.number_input("Sex")
bmi = st.number_input("BMI")
bp = st.number_input("Blood Pressure")
s1 = st.number_input("S1")
s2 = st.number_input("S2")
s3 = st.number_input("S3")
s4 = st.number_input("S4")
s5 = st.number_input("S5")
s6 = st.number_input("S6")

if st.button("Predict Progression"):
    try:
        # Convert input to float and form feature array
        features = [float(age), float(sex), float(bmi), float(bp), float(s1), float(s2), float(s3), float(s4), float(s5), float(s6)]
        features = np.array(features).reshape(1, -1)
        prediction = model.predict(features)
        st.success(f"Predicted Disease Progression: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Invalid input: {e}")
