import streamlit as st
import pandas as pd
import os

st.title("📊 Financial Data Explorer")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(BASE_DIR, "Data", "featured_emi_dataset.csv")

df = pd.read_csv(data_path)

st.write("Dataset Preview")
st.dataframe(df.head())

st.write("Eligibility Distribution")
st.bar_chart(df["emi_eligibility"].value_counts())
