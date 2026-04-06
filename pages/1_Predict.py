import streamlit as st
import joblib
import os
import pandas as pd
import numpy as np

st.set_page_config(page_title="Fraud Detection", page_icon="🔍", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');
html, body, [class*="css-"], [class*="st-"] {
    font-family: 'DM Sans', sans-serif !important;
}
section[data-testid="stSidebar"] {
    background: #faf8f6 !important;
}
</style>
""", unsafe_allow_html=True)

# Load model
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
model_path = os.path.join(BASE_DIR, "fraud_model.pkl")
data_path = os.path.join(BASE_DIR, "processed_fraud_data.csv")

model = joblib.load(model_path)
df = pd.read_csv(data_path)

st.title("Fraud Detection")

# ---------------- RANDOM TRANSACTION ----------------
st.markdown("### Test with Random Transaction")

if st.button("Generate Random Transaction"):
    sample = df.select_dtypes(include=["number"]).drop("Class", axis=1).sample(1)

    prob = model.predict_proba(sample)[0][1]

    st.write("Sample Transaction:")
    st.dataframe(sample)

    st.subheader(f"Fraud Probability: {prob:.4f}")

    if prob > 0.12:
        st.error("Fraud Detected")
    else:
        st.success("Legitimate Transaction")