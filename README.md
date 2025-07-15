# Diabetes Progression Predictor
This project is a machine learning application built using Scikit-learn and Streamlit. It predicts the disease progression in diabetes patients based on 10 physiological features. The app allows users to input patient data and get predictions instantly via a user-friendly web interface.
# Live Demo
[Live Demo](https://diabetes-predictor-0092.streamlit.app/)

# Project Structure
.
├── model.pkl                # Trained linear regression model (saved using joblib)
├── app.py                  # Streamlit app for prediction
├── train_model.py           # Script to train and save the model
├──requirement.txt            # All required libraries.
└── README.md               # Project documentation


# Model Overview
Dataset: Diabetes dataset from sklearn.datasets
Algorithm: Linear Regression
Target: A quantitative measure of disease progression one year after baseline

# User Inputs in App
The app takes the following 10 input features:
Age
Sex (Male or Female)
Body Mass Index (BMI)
Average Blood Pressure
Total Cholesterol (S1)
LDL Cholesterol (S2)
HDL Cholesterol (S3)
Cholesterol/HDL Ratio (S4)
Log of Serum Triglycerides (S5)
Glucose Serum Level (S6)

# Output
Once you input the values and click "Predict Progression", the app uses the trained model to display : Predicted Disease Progression:<some value>.
