import streamlit as st

st.set_page_config(
    page_title="CrediSense AI",
    page_icon="💳",
    layout="wide"
)

# -------- PREMIUM GLOBAL STYLES --------
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg,#eef2ff,#f8fbff);
    font-family: "Segoe UI", sans-serif;
}

/* Hide default app label */
section[data-testid="stSidebarNav"] > div:first-child {
    display:none;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#1e3a8a,#2563eb);
    color:white;
}
section[data-testid="stSidebar"] * {
    color:white !important;
}

/* Buttons */
.stButton button {
    background: linear-gradient(90deg,#2563eb,#4f46e5);
    color:white;
    border-radius:8px;
    padding:8px 22px;
    border:none;
    font-weight:600;
}
.stButton button:hover {
    background: linear-gradient(90deg,#1d4ed8,#4338ca);
}

/* Inputs */
div[data-baseweb="input"] {
    border-radius:10px !important;
    background:#f1f5ff !important;
}

/* Premium card container */
.card {
    background:white;
    padding:35px;
    border-radius:16px;
    box-shadow:0 8px 30px rgba(0,0,0,0.08);
    max-width:850px;
    margin:auto;
}

</style>
""", unsafe_allow_html=True)

# -------- SIDEBAR BRAND --------
st.sidebar.markdown("## 💳 **CrediSense AI**")
st.sidebar.caption("Smart Loan & EMI Intelligence System")

# -------- DEFAULT HOME --------
st.markdown("""
<div class="card" style='text-align:center;'>

<h1 style='margin-bottom:10px;'>🏦 EMI Predict AI Platform</h1>

<h3 style='color:#4b5563;'>Welcome to CrediSense AI</h3>

<br>

<h2 style='margin-top:25px;'>What this platform does</h2>

<p style='font-size:18px;'>
<strong>AI Eligibility Check</strong><br>
We analyse your financial profile and predict if taking a loan is safe.
</p>

<p style='font-size:18px;'>
<strong>Smart EMI Recommendation</strong><br>
Our model calculates an EMI that keeps your finances stable.
</p>

<br>

<p style='color:#6b7280;'>Use the sidebar to begin prediction.</p>

</div>
""", unsafe_allow_html=True)