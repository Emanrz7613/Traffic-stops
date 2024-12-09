# Streamlit App File
import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Traffic Stop Analysis App")

# Initialize session state for storing user inputs
if 'data' not in st.session_state:
    st.session_state['data'] = {}

# Home Page
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image("charlotte_cmpd_logo.jpg", width=320)
st.markdown("</div>", unsafe_allow_html=True)

st.title("Traffic Stop Analysis App")
st.write("""
This app predicts whether a search is likely to be conducted during a traffic stop and the probable outcome of the stop based on input details. Enter the traffic stop information to receive predictions and gain insights into traffic stop practices.
""")

# Home Page Content
st.sidebar.success("Navigate to the desired page using the sidebar.")

# Stop Information Section
st.header("App Information")



st.write("""
This app consists of three main pages:

1. **Data Exploration**: Information about this project and app
2. **Traffic Stop Outcome Prediction**: Predicts the probability of the result of the traffic stop.
3. **Traffic Stop Search Prediction**: Predicts whether a search will be conducted during a traffic stop.
         
    Please use the sidebar to navigate through the pages.
""")



