import streamlit as st
import pandas as pd
import pickle

# Load pre-trained model
with open('search_prediction_model.pkl', 'rb') as file:
    search_model = pickle.load(file)

st.title("Traffic Stop Search Prediction")
st.write("Enter the details of the traffic stop to predict if a search will be conducted.")

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
if st.button("Predict Search Conducted"):
    prediction = search_model.predict(input_data)[0]
    if prediction == 1:
        st.write("A search is likely to be conducted during the traffic stop.")
    else:
        st.write("A search is not likely to be conducted during the traffic stop.")