   
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


# Ensure session state is initialized for page
if 'page' not in st.session_state:
    st.session_state['page'] = 'Search_Prediction'

try:
    # Load pre-trained model
    with open('search_modelx.pkl', 'rb') as file:
        search_model = pickle.load(file)

    # Load pre-trained scaler
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)

    st.title("Traffic Stop Search Prediction")
    st.write("Enter details of the traffic stop to predict if a search will be conducted.")

    # Sidebar dropdown menus for the Search Prediction page
    st.sidebar.header("Search Prediction Input Features")

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
    
   
    
    
    

    # Store selected features in session state to be used by other pages

    st.session_state['Driver_Age'] = Driver_Age if Driver_Age else None
    st.session_state['CMPD_Division'] = CMPD_Division if CMPD_Division != "Select an option" else None
    st.session_state['Reason_for_Stop'] = Reason_for_Stop if Reason_for_Stop != "Select an option" else None
    st.session_state['Driver_Gender'] = Driver_Gender if Driver_Gender != "Select an option" else None
    st.session_state['Driver_Race'] = Driver_Race if Driver_Race != "Select an option" else None
    st.session_state['Officer_Gender'] = Officer_Gender if Officer_Gender != "Select an option" else None
    st.session_state['Driver_Ethnicity'] = Driver_Ethnicity if Driver_Ethnicity != "Select an option" else None

    # Prepare input data for model prediction
    input_features = {
        'Driver_Age': Driver_Age,
    }

    # Add categorical features with exact names expected by the model
    if CMPD_Division != "Select an option":
        input_features[f'CMPD_Division_{CMPD_Division}'] = 1

    if Reason_for_Stop != "Select an option":
        input_features[f'Reason_for_Stop_{Reason_for_Stop}'] = 1

    if Driver_Gender != "Select an option":
        input_features[f'Driver_Gender_{Driver_Gender}'] = 1

    if Driver_Race != "Select an option":
        input_features[f'Driver_Race_{Driver_Race}'] = 1

    if Officer_Gender != "Select an option":
        input_features[f'Officer_Gender_{Officer_Gender}'] = 1

    if Driver_Ethnicity != "Select an option":
        input_features[f'Driver_Ethnicity_{Driver_Ethnicity}'] = 1

    # Fill missing dummy variables with 0
    all_features = search_model.feature_names_in_

        # Create input data DataFrame and ensure feature names match exactly
    input_data = pd.DataFrame([{k: input_features.get(k, 0) for k in all_features}], columns=all_features)

    # Assign feature names
    input_data.columns = all_features

        # Scale numerical features
    numerical_features = ['Driver_Age']
    input_data[numerical_features] = scaler.transform(input_data[numerical_features])

    # Predict
    if st.button("Predict Search Conducted"):
        if input_data.empty:
            st.write("Please provide all required inputs before predicting.")
        else:
            try:
                probabilities = search_model.predict_proba(input_data)[0]
                prediction = search_model.predict(input_data)[0]

                # Display prediction result
                if prediction == 1:
                    st.markdown("<h2 style='color: red;'>A search is likely to be conducted during the traffic stop.</h2>", unsafe_allow_html=True)
                    st.markdown("<div style='text-align: center;'><img src='https://gifdb.com/images/high/police-car-lights-on-top-a2uurw8a7w28z1xm.webp' width='300' style='display: block; margin-left: auto; margin-right: auto;'></div>", unsafe_allow_html=True)
                else:
                    st.markdown("<h2 style='color: green; text-align: center;'>A search is not likely to be conducted during the traffic stop.</h2>", unsafe_allow_html=True)
                    st.markdown("<div style='text-align: center;'><img src='https://gifdb.com/images/high/happy-dance-celebrate-meme-m8pmc10c5p736lcs.webp' width='300' style='display: block; margin-left: auto; margin-right: auto;'></div>", unsafe_allow_html=True)

                # Display pie chart of probabilities
                labels = ['No Search', 'Search']
                sizes = [probabilities[0], probabilities[1]]
                colors = ['green', 'red']
                
                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor': 'black'})
                ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                st.pyplot(fig)
            except Exception as e:
                st.error("An error occurred during prediction.")

except FileNotFoundError as e:
    st.error("Required file not found: " + str(e))
except Exception as e:
    st.error("An unexpected error occurred: " + str(e))

    
    # Scale numerical features
    numerical_features = ['Driver_Age']
    input_data[numerical_features] = scaler.transform(input_data[numerical_features])

    # Predict
    if st.button("Predict Search Conducted"):
        if input_data.empty:
            st.write("Please provide all required inputs before predicting.")
        else:
            try:
                probabilities = search_model.predict_proba(input_data)[0]
                prediction = search_model.predict(input_data)[0]

                # Display prediction result
                if prediction == 1:
                    st.markdown("<h2 style='color: red;'>A search is likely to be conducted during the traffic stop.</h2>", unsafe_allow_html=True)
                    st.markdown("<div style='text-align: center;'><img src='https://gifdb.com/images/high/police-car-lights-on-top-a2uurw8a7w28z1xm.webp' width='300' style='display: block; margin-left: auto; margin-right: auto;'></div>", unsafe_allow_html=True)
                else:
                    st.markdown("<h2 style='color: green; text-align: center;'>A search is not likely to be conducted during the traffic stop.</h2>", unsafe_allow_html=True)
                    st.markdown("<div style='text-align: center;'><img src='https://gifdb.com/images/high/happy-dance-celebrate-meme-m8pmc10c5p736lcs.webp' width='300' style='display: block; margin-left: auto; margin-right: auto;'></div>", unsafe_allow_html=True)

                # Display pie chart of probabilities
                labels = ['No Search', 'Search']
                sizes = [probabilities[0], probabilities[1]]
                colors = ['green', 'red']
                
                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor': 'black'})
                ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                st.pyplot(fig)
            except Exception as e:
                st.error("An error occurred during prediction.")

except FileNotFoundError as e:
    st.error("Required file not found: " + str(e))
except Exception as e:
    st.error("An unexpected error occurred: " + str(e))
