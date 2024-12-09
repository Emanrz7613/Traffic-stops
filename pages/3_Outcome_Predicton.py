import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb
import numpy as np

# Load the XGBoost model, encoder, and pre-trained resources
xgb_model = xgb.Booster()
xgb_model.load_model('outcome_model.json')
outcome_encoder = joblib.load('outcome_encoder.joblib')

st.title("Traffic Stop Outcome Prediction")
st.write("Determine the Probability of Different Results of Your Traffic Stop")

# Sidebar dropdown menus for the Outcome Prediction page
st.sidebar.header("Outcome Prediction Input Features")

# Helper function to get index for selectbox
def get_selectbox_index(options, value):
    if value is None or value not in options:
        return 0
    return options.index(value) + 1

# Extracted unique values for dropdown menus
cmpd_divisions = ["South Division", "Independence Division", "University City Division", "Metro Division", "Freedom Division", "Providence Division", "Westover Division", "Eastway Division", "Hickory Grove Division", "North Division", "Steele Creek Division", "North Tryon Division", "Central Division"]
reasons_for_stop = ["Speeding", "Vehicle Regulatory", "Stop Light/Sign", "Vehicle Equipment", "Other", "Safe Movement", "Investigation", "SeatBelt", "Driving While Impaired", "CheckPoint"]
driver_races = ["Asian", "White", "Black", "Other/Unknown", "Native American"]
driver_genders = ["Female", "Male"]
officer_genders = ["Male", "Female"]
driver_ethnicities = ["Non-Hispanic", "Hispanic"]

# Use values from session state to populate sidebar inputs
Driver_Age = st.sidebar.number_input("Driver Age", min_value=16, max_value=100, value=st.session_state.get('Driver_Age', None), step=1)
Driver_Gender = st.sidebar.selectbox("Driver Gender", ["Select an option"] + driver_genders, index=get_selectbox_index(driver_genders, st.session_state.get('Driver_Gender', None)))
Driver_Race = st.sidebar.selectbox("Driver Race", ["Select an option"] + driver_races, index=get_selectbox_index(driver_races, st.session_state.get('Driver_Race', None)))
Driver_Ethnicity = st.sidebar.selectbox("Driver Ethnicity", ["Select an option"] + driver_ethnicities, index=get_selectbox_index(driver_ethnicities, st.session_state.get('Driver_Ethnicity', None)))
Officer_Gender = st.sidebar.selectbox("Officer Gender", ["Select an option"] + officer_genders, index=get_selectbox_index(officer_genders, st.session_state.get('Officer_Gender', None)))
Reason_for_Stop = st.sidebar.selectbox("Reason for Stop", ["Select an option"] + reasons_for_stop, index=get_selectbox_index(reasons_for_stop, st.session_state.get('Reason_for_Stop', None)))
CMPD_Division = st.sidebar.selectbox("CMPD Division", ["Select an option"] + cmpd_divisions, index=get_selectbox_index(cmpd_divisions, st.session_state.get('CMPD_Division', None)))

# Store selected features in session state
st.session_state['Driver_Age'] = Driver_Age if Driver_Age else None
st.session_state['CMPD_Division'] = CMPD_Division if CMPD_Division != "Select an option" else None
st.session_state['Reason_for_Stop'] = Reason_for_Stop if Reason_for_Stop != "Select an option" else None
st.session_state['Driver_Gender'] = Driver_Gender if Driver_Gender != "Select an option" else None
st.session_state['Driver_Race'] = Driver_Race if Driver_Race != "Select an option" else None
st.session_state['Officer_Gender'] = Officer_Gender if Officer_Gender != "Select an option" else None
st.session_state['Driver_Ethnicity'] = Driver_Ethnicity if Driver_Ethnicity != "Select an option" else None

# Prepare input data for model prediction
input_data = {
    'Reason_for_Stop': Reason_for_Stop,
    'Officer_Gender': Officer_Gender,
    'Driver_Race': Driver_Race,
    'Driver_Ethnicity': Driver_Ethnicity,
    'Driver_Gender': Driver_Gender,
    'Driver_Age': Driver_Age,
    'CMPD_Division': CMPD_Division
}

# Convert input data to a DataFrame
input_df = pd.DataFrame([input_data])

# Ensure categorical features are of the 'category' dtype
categorical_columns = ['Reason_for_Stop', 'Officer_Gender', 'Driver_Race', 'Driver_Ethnicity', 'Driver_Gender', 'CMPD_Division']
input_df[categorical_columns] = input_df[categorical_columns].astype('category')

# Predict
if st.button("Predict Outcome Probability"):
    try:
        dmatrix_input = xgb.DMatrix(input_df, enable_categorical=True)
        probabilities = xgb_model.predict(dmatrix_input)

        # Decode class labels
        if probabilities.ndim == 1:
            probabilities = np.expand_dims(probabilities, axis=0)
        predicted_label_index = np.argmax(probabilities[0])
        predicted_label = outcome_encoder.classes_[predicted_label_index]
        probabilities_percent = probabilities[0] * 100

        # Display the prediction result for sidebar input
        st.markdown(f"### Likely Outcome: {predicted_label}")
        st.write("### Outcome Probabilities:")
        sorted_indices = np.argsort(-probabilities[0])
        for idx in sorted_indices:
            st.write(f"{outcome_encoder.classes_[idx]}: {probabilities_percent[idx]:.2f}%")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")









