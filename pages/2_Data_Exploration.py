import streamlit as st
import pandas as pd

# Set custom page configuration with page title
st.set_page_config(page_title="Traffic Stops: Data Exploration")

st.title("Traffic Stops: A Data-Driven Exploration")

# Problem Section
st.header("The Challenge")
st.write("""
- **Key Question:** What factors influence the outcomes of traffic stops in the city?
- **Goals:**
  - Identify trends and patterns in traffic stop outcomes.
  - Build a predictive model to assess potential outcomes based on specific input factors.
  - Provide actionable insights to law enforcement for improving fairness and efficiency.
""")

# Data Highlights Section
st.header("Data Highlights")
st.write("""
### Data Source:
- Publicly available traffic stop data for the city.

### Key Highlights:
- **Data Size:** 100,000+ records of traffic stops.
- **Features:** 7 predictors, including:
  - *Reason for Stop*
  - *Driver Demographics (Race, Ethnicity, Age, Gender)*
  - *Officer Gender*
  - *CMPD Division*
- **Target Variable:** Outcome of stop (e.g., Citation, Verbal Warning, Arrest).

### Challenges and Engineering:
- Handling categorical variables with multiple levels.
- Balancing the dataset for underrepresented outcomes.
- Dealing with missing and inconsistent entries.
""")

# Exploratory Data Analysis Section
st.header("Exploratory Data Analysis")
st.write("""
### Key Observations:
- *Reason for Stop* is the most critical feature based on initial trends.
- Certain divisions showed higher frequencies of specific outcomes.
- Disparities in stop outcomes based on demographic factors prompted hypotheses:
  - **Hypothesis 1:** Reason for Stop will significantly influence outcomes.
  - **Hypothesis 2:** Driver demographics (age, race, ethnicity) will contribute to outcome predictions.

### Influence on Approach:
- EDA highlighted the importance of categorical encoding and ensuring fairness in the model.
""")

# Modeling Section
st.header("Modeling")
st.write("""
### Why LightGBM?
- Handles categorical data efficiently with minimal preprocessing.
- Built-in capabilities for imbalanced datasets and multiclass classification.
- Faster training and scalability compared to alternatives like XGBoost and Neural Networks.

### Optimization:
- **Parameter Tuning:** Randomized search to optimize hyperparameters:
  - Learning rate, number of leaves, max depth, subsample ratio, etc.
- Balanced dataset using stratified sampling.
""")

# Results Section
st.header("Results")
st.write("""
### Quantitative Evaluation:
- **Accuracy:** 78% (multiclass classification).
- **AUC (One-vs-Rest):** 0.85.

### Feature Importance:
1. Reason for Stop (45%)
2. CMPD Division (13%)
3. Driver Ethnicity (10%)

### Qualitative Insights:
- Stronger performance for frequent outcomes (e.g., Citations).
- Struggles with rare classes (e.g., Arrests).
- Predictions align with known traffic stop patterns.
""")

# So What? Section
st.header("So What?")
st.write("""
### Applications:
- Predictive tool for law enforcement to prioritize resources.
- Insights to address potential biases in traffic stop practices.
- Data-driven approach to improving public trust and safety.

### Surprises:
- "Reason for Stop" dominated feature importance.
- "Driver Age" had limited predictive power compared to other features.
""")

# Challenges and Learning Opportunities Section
st.header("Challenges and Learning Opportunities")
st.write("""
### Challenges:
- Balancing multiple target classes with significant class imbalance.
- Ensuring model interpretability while maintaining accuracy.

### Learning Opportunities:
- Leveraging LightGBM’s categorical handling streamlined preprocessing.
- Feature importance insights reshaped initial assumptions about age.

### Future Directions:
- Explore ensemble methods to boost rare class performance.
- Incorporate additional data points, like time of day or officer experience, for better context.
""")

# Conclusion Section
st.header("Conclusion")
st.write("""
- A data-driven approach to understanding traffic stops can improve fairness and outcomes.
- LightGBM proved effective but leaves room for refinement.
- This project sets the stage for actionable insights and further research.
""")








