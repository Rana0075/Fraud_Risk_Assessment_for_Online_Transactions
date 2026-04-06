import streamlit as st


st.set_page_config(
    page_title="FraudShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap');
html, body, [class*="css-"], [class*="st-"] { font-family: 'DM Sans', sans-serif !important; }
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: rgba(0,0,0,0) !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 3rem !important; }
section[data-testid="stSidebar"] { background: #ffffff !important; }
.scard {
    background:#fff; border:1px solid #e8e6e1; border-radius:12px;
    padding:22px 16px; text-align:center;
    box-shadow:0 1px 3px rgba(0,0,0,.03), 0 4px 12px rgba(0,0,0,.02);
    position:relative; overflow:hidden; transition:all .25s;
}
.scard:hover { transform:translateY(-2px); box-shadow:0 4px 20px rgba(0,0,0,.05); }
.scard::after { content:''; position:absolute; bottom:0; left:0; right:0; height:3px; }
.scard.t::after { background:#0d9488; } .scard.r::after { background:#dc2626; }
.scard.a::after { background:#d97706; } .scard.p::after { background:#7c3aed; }
.tcard {
    background:#fff; border:1px solid #e8e6e1; border-radius:12px;
    padding:18px 20px; display:flex; align-items:center; gap:14px;
    box-shadow:0 1px 3px rgba(0,0,0,.03), 0 4px 12px rgba(0,0,0,.02);
    transition:all .25s;
}
.tcard:hover { border-color:#ddd; transform:translateY(-1px); }
.tav {
    width:44px; height:44px; border-radius:10px;
    display:flex; align-items:center; justify-content:center;
    font-size:15px; font-weight:700; color:#fff; flex-shrink:0;
}
.hero {
    background:#fff; border:1px solid #e8e6e1; border-radius:14px;
    padding:44px 40px;
    box-shadow:0 2px 4px rgba(0,0,0,.03), 0 12px 40px rgba(0,0,0,.04);
    position:relative; overflow:hidden;
}
.hero::after {
    content:''; position:absolute; top:-60px; right:-60px;
    width:220px; height:220px;
    background:radial-gradient(circle, rgba(13,148,136,0.1), transparent 70%);
    border-radius:50%; pointer-events:none;
}
.badge {
    display:inline-flex; align-items:center; gap:5px;
    font-size:10.5px; text-transform:uppercase; letter-spacing:1.2px;
    color:#0d9488; background:rgba(13,148,136,0.08);
    padding:5px 12px; border-radius:99px; font-weight:600; margin-bottom:16px;
}
.card {
    background:#fff; border:1px solid #e8e6e1; border-radius:14px;
    padding:24px;
    box-shadow:0 1px 3px rgba(0,0,0,.03), 0 6px 16px rgba(0,0,0,.025);
    transition:all .25s;
}
.card:hover { box-shadow:0 2px 6px rgba(0,0,0,.04), 0 10px 30px rgba(0,0,0,.05); }
.slabel {
    font-size:11px; font-weight:700; text-transform:uppercase;
    letter-spacing:1.5px; color:#888; margin-bottom:12px;
}
.cl { list-style:none; padding:0; margin:0; }
.cl li { font-size:13px; color:#666; padding:4px 0; line-height:1.6; }
.cl li i { color:#0d9488; font-size:10px; margin-right:8px; }
.bl {
    display:inline-flex; align-items:center; gap:7px;
    padding:10px 22px; border-radius:8px;
    font-size:13.5px; font-weight:600; text-decoration:none;
    transition:all 0.2s;
}
.bl-p { background:#0d9488; color:#fff; box-shadow:0 2px 10px rgba(13,148,136,0.2); }
.bl-p:hover { background:#0f766e; }
.bl-o { background:transparent; color:#1a1a2e; border:1px solid #d5d2cc; }
.bl-o:hover { border-color:#0d9488; color:#0d9488; }
</style>""", unsafe_allow_html=True)

# ── Hero ──
st.markdown("""<div class="hero">
<div class="badge"><i class="fas fa-shield-halved"></i> Fraud Risk Assessment</div>
<h1 style="font-size:30px;font-weight:800;letter-spacing:-0.6px;line-height:1.15;margin-bottom:10px;max-width:580px;">
Fraud Risk Assessment for <span style="color:#0d9488;">Online Transactions</span></h1>
<p style="color:#777;font-size:14px;line-height:1.7;max-width:540px;margin-bottom:24px;">
A machine learning–based fraud detection system that analyzes historical transaction data to identify fraudulent patterns and supports cost-sensitive decision-making.</p>
</div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Quick stats
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        '<div class="scard t">'
        '<div style="font-size:26px;font-weight:800;color:#0d9488;">80%</div>'
        '<div style="font-size:10px;color:#999;font-family:monospace;text-transform:uppercase;letter-spacing:1px;">Recall (Fraud Caught)</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        '<div class="scard r">'
        '<div style="font-size:26px;font-weight:800;color:#16a34a;">89%</div>'
        '<div style="font-size:10px;color:#999;font-family:monospace;text-transform:uppercase;letter-spacing:1px;">Precision</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        '<div class="scard a">'
        '<div style="font-size:26px;font-weight:800;color:#dc2626;">9</div>'
        '<div style="font-size:10px;color:#999;font-family:monospace;text-transform:uppercase;letter-spacing:1px;">False Positives</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        '<div class="scard p">'
        '<div style="font-size:26px;font-weight:800;color:#7c3aed;">76</div>'
        '<div style="font-size:10px;color:#999;font-family:monospace;text-transform:uppercase;letter-spacing:1px;">Frauds Detected</div>'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# Team — 2 members
st.markdown('<div class="slabel"><i class="fas fa-users" style="color:#0d9488;margin-right:6px;font-size:12px;"></i>Team Members</div>', unsafe_allow_html=True)
t1, t2 = st.columns(2)
with t1:
    st.markdown("""
    <div class="tcard">
        <div class="tav" style="background:linear-gradient(135deg,#0d9488,#06b6d4);">TR</div>
        <div>
            <div style="font-size:14px;font-weight:700;color:#1a1a2e;">Tannu Rana</div>
            <div style="font-size:12px;color:#0d9488;font-weight:500;">26E4103-WhileLoop</div>
            <div style="font-size:10.5px;color:#999;font-family:monospace;margin-top:2px;">ID: 2201730093</div>
        </div>
    </div>""", unsafe_allow_html=True)
with t2:
    st.markdown("""
    <div class="tcard">
        <div class="tav" style="background:linear-gradient(135deg,#d97706,#f59e0b);">NS</div>
        <div>
            <div style="font-size:14px;font-weight:700;color:#1a1a2e;">Nisha Sharma</div>
            <div style="font-size:12px;color:#0d9488;font-weight:500;">26E4103-WhileLoop</div>
            <div style="font-size:10.5px;color:#999;font-family:monospace;margin-top:2px;">ID: 2201730080</div>
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Project description
st.markdown('<div class="slabel"><i class="fas fa-folder-open" style="color:#0d9488;margin-right:6px;font-size:12px;"></i>Project Description</div>', unsafe_allow_html=True)
d1, d2 = st.columns(2)
with d1:
    st.markdown("""
    <div class="card">
        <h3 style="font-size:14.5px;font-weight:700;margin-bottom:10px;display:flex;align-items:center;gap:7px;">
            <i class="fas fa-bullseye" style="color:#0d9488;font-size:13px;"></i>Problem Description</h3>
        <p style="font-size:13px;color:#666;line-height:1.7;">
        With the rapid growth of online payments and e-commerce platforms, fraudulent transactions have become a significant challenge for businesses and financial institutions. Fraudulent activities result in direct financial losses, increased operational costs, and reduced customer trust. At the same time, incorrectly flagging legitimate transactions as fraudulent can negatively impact user experience and lead to customer dissatisfaction.</p>
    </div>
    <div style="height:12px"></div>
    <div class="card">
        <h3 style="font-size:14.5px;font-weight:700;margin-bottom:10px;display:flex;align-items:center;gap:7px;">
            <i class="fas fa-cogs" style="color:#0d9488;font-size:13px;"></i>Proposed Solution</h3>
        <p style="font-size:13px;color:#666;line-height:1.7;">
        Using supervised machine learning techniques to assess fraud risk based on historical online transaction data. The approach includes data preprocessing, exploratory data analysis, and feature engineering to extract relevant transaction characteristics. Classification models are trained and evaluated with a focus on precision–recall tradeoffs to support effective fraud risk assessment.</p>
    </div>""", unsafe_allow_html=True)
with d2:
    st.markdown("""
    <div class="card">
        <h3 style="font-size:14.5px;font-weight:700;margin-bottom:10px;display:flex;align-items:center;gap:7px;">
            <i class="fas fa-list-check" style="color:#0d9488;font-size:13px;"></i>Objectives</h3>
        <ul class="cl">
            <li><i class="fas fa-check"></i>Analyze transaction data and identify patterns associated with fraudulent activity</li>
            <li><i class="fas fa-check"></i>Address the issue of class imbalance in fraud detection datasets</li>
            <li><i class="fas fa-check"></i>Develop a machine learning–based model for assessing fraud risk in online transactions</li>
            <li><i class="fas fa-check"></i>Evaluate model performance using precision, recall, and confusion matrix</li>
            <li><i class="fas fa-check"></i>Study the tradeoff between fraud detection and false positive rates</li>
        </ul>
    </div>
    <div style="height:12px"></div>
    <div class="card">
        <h3 style="font-size:14.5px;font-weight:700;margin-bottom:10px;display:flex;align-items:center;gap:7px;">
            <i class="fas fa-flask" style="color:#0d9488;font-size:13px;"></i>Technology Stack</h3>
        <ul class="cl">
            <li><i class="fas fa-check"></i><b>Python</b> — Pandas, NumPy, Scikit-learn</li>
            <li><i class="fas fa-check"></i><b>ML Models</b> — Logistic Regression, Random Forest, XGBoost</li>
            <li><i class="fas fa-check"></i><b>Evaluation</b> — Precision, Recall, Confusion Matrix</li>
            <li><i class="fas fa-check"></i><b>Deployment</b> — Streamlit</li>
        </ul>
    </div>""", unsafe_allow_html=True)