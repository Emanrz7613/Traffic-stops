import streamlit as st
import pandas as pd

# Set custom page configuration with page title
st.set_page_config(page_title="Home")





st.title("Traffic Stop Information")
st.write("Enter the information pertaining to your traffic stop")

st.sidebar.success("Select a page above to navigate.")

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

# Extracted dropdown menus and input fields
Driver_Age = st.number_input("Driver Age", min_value=16, max_value=100, value=st.session_state.get('Driver_Age', None), step=1)
CMPD_Division = st.selectbox("CMPD Division", ["Select an option"] + cmpd_divisions, index=get_selectbox_index(cmpd_divisions, st.session_state.get('CMPD_Division', None)))
Reason_for_Stop = st.selectbox("Reason for Stop", ["Select an option"] + reasons_for_stop, index=get_selectbox_index(reasons_for_stop, st.session_state.get('Reason_for_Stop', None)))
Driver_Gender = st.selectbox("Driver Gender", ["Select an option"] + driver_genders, index=get_selectbox_index(driver_genders, 'Male' if st.session_state.get('Driver_Gender', None) == 1 else 'Female'))
Driver_Race = st.selectbox("Driver Race", ["Select an option"] + driver_races, index=get_selectbox_index(driver_races, st.session_state.get('Driver_Race', None)))
Officer_Gender = st.selectbox("Officer Gender", ["Select an option"] + officer_genders, index=get_selectbox_index(officer_genders, 'Male' if st.session_state.get('Officer_Gender', None) == 1 else 'Female'))
Driver_Ethnicity = st.selectbox("Driver Ethnicity", ["Select an option"] + driver_ethnicities, index=get_selectbox_index(driver_ethnicities, st.session_state.get('Driver_Ethnicity', None)))

# Store selected features in session state to be used by other pages
st.session_state['Driver_Age'] = Driver_Age if Driver_Age else None
st.session_state['CMPD_Division'] = CMPD_Division if CMPD_Division != "Select an option" else None
st.session_state['Reason_for_Stop'] = Reason_for_Stop if Reason_for_Stop != "Select an option" else None
st.session_state['Driver_Gender'] = 1 if Driver_Gender == 'Male' else (0 if Driver_Gender == 'Female' else None)
st.session_state['Driver_Race'] = Driver_Race if Driver_Race != "Select an option" else None
st.session_state['Officer_Gender'] = 1 if Officer_Gender == 'Male' else (0 if Officer_Gender == 'Female' else None)
st.session_state['Driver_Ethnicity'] = Driver_Ethnicity if Driver_Ethnicity != "Select an option" else None

st.write("""
This page allows you to select input features that will be used for both **Traffic Stop Search Prediction** and **Outcome Prediction** models.
""")
