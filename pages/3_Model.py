import streamlit as st
import pandas as pd

st.set_page_config(page_title="Model Performance", page_icon="🏆", layout="wide")

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

st.title("Model Performance")

data = {
    "Model": ["Random Forest", "XGBoost", "Logistic Regression"],
    "Precision": [0.89, 0.98, 0.85],
    "Recall": [0.80, 0.76, 0.76],
    "F1 Score": [0.84, 0.857, 0.80]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.markdown("### Final Decision")

st.write("""
Random Forest was selected because it provides the best balance 
between precision and recall.

A lower threshold (0.12) was chosen to prioritize fraud detection
and reduce missed fraudulent transactions.
""")