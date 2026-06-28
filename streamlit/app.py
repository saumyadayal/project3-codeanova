import streamlit as st

st.set_page_config(
    page_title="ChurnShield",
    page_icon="📊",
    layout="wide"
)

st.title("📊 ChurnShield")

st.markdown("""
## Customer Churn Prediction Dashboard

This dashboard predicts whether a telecom customer is likely to churn using Machine Learning.

Developed as part of the **Code A Nova Data Science Internship**.
""")

st.success("Machine Learning Model Integrated")

st.header("Demo Prediction")

gender = st.selectbox("Gender",["Male","Female"])

tenure = st.slider("Tenure",0,72,12)

monthly = st.slider("Monthly Charges",0,150,75)

contract = st.selectbox(
    "Contract",
    ["Month-to-month","One year","Two year"]
)

if st.button("Predict Churn"):

    st.warning("Prediction functionality will be connected to the trained model.")
