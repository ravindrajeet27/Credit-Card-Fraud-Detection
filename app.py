import pandas as pd
import joblib

model = joblib.load("fraud_detection_model.joblib")

import streamlit as st

st.set_page_config(page_title="Fraud Detection System",
                   page_icon="🔍",
                   layout="wide")

menu = st.sidebar.radio(
    "Navigation",
    ["Home",
     "Model Performance",
     "Single Prediction",
     "Batch Prediction",
     "About Project"]
)

if menu == "Home":

    st.title("💳 Credit Card Fraud Detection")

    st.write("""
    This application detects fraudulent credit card transactions
    using a Machine Learning model trained on historical transaction data.
    """)

    st.success("Model Ready for Prediction")
if menu == "Model Performance":

    st.title("📊 Model Performance")

    col1, col2, col3 = st.columns(3)

    col1.metric("Accuracy", "99.9%")
    col2.metric("Precision", "92%")
    col3.metric("Recall", "89%")

    st.write("ROC-AUC Score: 0.98")

import numpy as np





if menu == "Batch Prediction":

    st.title("📁 Upload Transactions")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.write(df.head())

        if st.button("Run Prediction"):

            predictions = model.predict(df)

            df["Prediction"] = predictions

            st.write(df.head())

            csv = df.to_csv(index=False)

            st.download_button(
                "Download Results",
                csv,
                "predictions.csv"
            )
if menu == "About Project":

    st.title("ℹ️ About Project")

    st.write("""
    Developed by Ravindrajeet Gautam

    Technologies Used:

    • Python
    • Pandas
    • Scikit-Learn
    • Streamlit
    • Random Forest Classifier

    Objective:
    Detect fraudulent transactions and reduce financial risk.
    """)