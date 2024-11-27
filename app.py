import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("salary_predictor_model.pkl")

# Streamlit App
st.title("HR Salary Prediction Dashboard")
st.write("Use this dashboard to predict the expected salary of HR professionals based on their age and years of experience.")

# Input fields
age = st.number_input("Enter Age:", min_value=18, max_value=65, step=1)
years_experience = st.number_input("Enter Years of Experience:", min_value=0, max_value=40, step=1)

# Prediction
if st.button("Predict Salary"):
    # Prepare the input features as per the model's requirements (only Age and Years of Experience)
    features = [[age, years_experience]]
    prediction = model.predict(features)
    
    # Display the predicted salary
    st.success(f"The predicted salary is: ₹{prediction[0]:,.2f}")
