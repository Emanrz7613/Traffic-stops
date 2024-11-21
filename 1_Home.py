# Streamlit App File
import streamlit as st
import pandas as pd

# Set custom page configuration with page title
st.set_page_config(page_title="Home")

# Display the image at the top of the page using st.image() with HTML for centering
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image("charlotte_cmpd_logo.jpg", width=320)
st.markdown("</div>", unsafe_allow_html=True)

st.title("Traffic Stop Analysis App")
st.write("The Charlotte-Mecklenburg Police Department (CMPD), conducts a significant number of traffic stops annually, averaging around 120,000 per year, and are required by North Carolina state law to collect detailed data on each stop, including the reason for the stop, actions taken, and driver demographics like race, ethnicity, and age, which is then reported to the NC Department of Justice; the CMPD focuses on deploying traffic officers to areas with high crime rates and community concerns, aiming to address safety issues proactively; data used to train these models can be accessed through the City of Charlotte Open Data Portal.")

# Ensure session state is initialized for page
if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

# Home Page Content
st.sidebar.success("Navigate to the Stop Information page to enter your information. You can also navigate directly to the model page you would like to use")

# Stop Information Section
st.header("App Information")



st.write("""
This app consists of three main pages:

1. **Traffic Stop Outcome Prediction**: Predicts the probability of the result of the traffic stop.
2. **Traffic Stop Search Prediction**: Predicts whether a search will be conducted during a traffic stop.
3. **Traffic Stop Information**: Enter the information about your stop to predict the outcomes.
         
    Please use the sidebar to navigate through the pages.
""")



