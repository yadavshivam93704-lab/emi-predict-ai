import streamlit as st
import pandas as pd

st.title("🛠️ Data Management Panel")

uploaded = st.file_uploader("Upload new financial dataset")

if uploaded:
    df = pd.read_csv(uploaded)
    st.success("Dataset uploaded successfully")
    st.dataframe(df.head())
