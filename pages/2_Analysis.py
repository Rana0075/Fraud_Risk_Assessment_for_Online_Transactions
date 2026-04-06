import streamlit as st
import pandas as pd

st.set_page_config(page_title="Transaction Analysis", page_icon="📊", layout="wide")



st.title("Transaction Analysis")
st.caption("Key insights from exploring the fraud detection dataset.")
st.markdown("---")

# 1
st.subheader("1. Severe Class Imbalance")
st.write("Fraud transactions are extremely rare (~0.17% of total data).")
with st.expander("Why it matters & what we did"):
    st.write("**Why it matters:**")
    st.write("- Accuracy becomes misleading (a dumb model can get 99% easily)")
    st.write("- Models tend to ignore fraud unless corrected")
    st.write("**What we did:**")
    st.write("- Used class_weight='balanced'")
    st.write("- Focused on precision, recall, F1 instead of accuracy")

st.markdown("---")

# 2
st.subheader("2. Fraud Shows Extreme Behavior in Amount")
st.write("Fraud is more likely in very small and very large transactions (U-shaped pattern).")
with st.expander("Interpretation & impact"):
    st.write("**Interpretation:**")
    st.write("- Small amounts → test transactions")
    st.write("- Large amounts → high-value fraud attempts")
    st.write("**Impact on model:**")
    st.write("- Amount (and LogAmount) becomes an important signal")

st.markdown("---")

# 3
st.subheader("3. Time-Based Pattern Exists")
st.write("Fraud is more frequent during night hours.")
with st.expander("Interpretation & features created"):
    st.write("**Interpretation:**")
    st.write("- Lower human monitoring")
    st.write("- Automated or unusual activity spikes")
    st.write("**Features created:** Hour, IsNight")
    st.write("**Impact:** Slight but meaningful improvement in detection")

st.markdown("---")

# 4
st.subheader("4. Certain Features Strongly Indicate Fraud")
st.write("Top correlated features: V17, V14, V12, V10")
with st.expander("Meaning & note"):
    st.write("These PCA components capture hidden fraud patterns.")
    st.warning("Features are anonymized → cannot interpret directly. But model still uses them effectively.")

st.markdown("---")

# 5
st.subheader("5. Not All Features Matter")
st.write("Low-impact features: V25, V15, V13, etc.")
with st.expander("Insight"):
    st.write("Some variables contribute little to fraud detection. Model naturally focuses on strong signals.")

st.markdown("---")

# 6
st.subheader("6. Threshold Matters More Than Model Choice")
st.write("Default threshold (0.5) was not optimal.")
with st.expander("After tuning"):
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Optimal Threshold", "0.12")
    with col2:
        st.metric("Recall Improved", "0.69 → 0.80")
    st.write("Model was too conservative initially. Lower threshold allowed better fraud detection.")

st.markdown("---")

# 7
st.subheader("7. Trade-off Between Precision and Recall")
st.write("Increasing recall always reduces precision.")
with st.expander("Real-world meaning"):
    st.write("- Higher recall → more fraud caught")
    st.write("- But → more false alarms")
    st.info("More security = more customer friction")

st.markdown("---")

# 8
st.subheader("8. Model Comparison Insight")
comp = pd.DataFrame({
    "Model": ["Logistic Regression", "Random Forest", "XGBoost"],
    "Behavior": [
        "High recall, very low precision (too aggressive)",
        "Best balance",
        "Very high precision, slightly lower recall"
    ]
})
st.dataframe(comp, use_container_width=True, hide_index=True)
st.success("Random Forest selected for balanced performance.")

st.markdown("---")

# 9
st.subheader("9. Model Performance Ceiling")
st.write("Recall plateaued around ~80%.")
with st.expander("Interpretation"):
    st.write("Even after tuning, further lowering threshold gave minimal gains.")
    st.write("Remaining fraud cases are hard to distinguish. Limitation is data/features, not model.")

st.markdown("---")

# 10
st.subheader("10. Final System Insight")
st.write("The model outputs probability, not decisions.")
with st.expander("How the system works"):
    st.code("Probability → Threshold → Decision", language="text")
    st.info("Key takeaway: Fraud detection is a decision system, not just a model.")

