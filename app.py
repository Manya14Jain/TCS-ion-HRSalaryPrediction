import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("salary_predictor_model.pkl")

# Streamlit App
st.title("HR Salary Prediction Dashboard")
st.write("Use this dashboard to predict the expected salary of HR professionals.")

# Input fields
age = st.number_input("Enter Age:", min_value=18, max_value=65, step=1)
years_experience = st.number_input("Years of Experience:", min_value=0, max_value=40, step=1)
current_salary = st.number_input("Current Salary:", min_value=20000, max_value=200000, step=1000)

# Prediction
if st.button("Predict Salary"):
    features = [[age, years_experience, current_salary]]
    prediction = model.predict(features)
    st.success(f"The predicted salary is: ₹{prediction[0]:,.2f}")
