import streamlit as st
import pandas as pd
import pickle

# Load pre-trained model
with open('outcome_prediction_model.pkl', 'rb') as file:
    outcome_model = pickle.load(file)

st.title("Traffic Stop Outcome Prediction")
st.write("Enter the details of the traffic stop to predict the outcome.")

# Example input features
driver_age = st.number_input("Driver Age", min_value=16, max_value=100, value=30)
driver_gender = st.selectbox("Driver Gender", ["Male", "Female"])
violation = st.selectbox("Violation", ["Speeding", "Seatbelt", "DUI", "Other"])

# Prepare input data
input_data = pd.DataFrame({
    'driver_age': [driver_age],
    'driver_gender': [1 if driver_gender == 'Male' else 0],
    'violation': [violation]
})

# Predict
if st.button("Predict Traffic Stop Outcome"):
    probability = outcome_model.predict_proba(input_data)[0][1]
    st.write(f"The probability of a positive outcome (e.g., a warning) is {probability * 100:.2f}%.")