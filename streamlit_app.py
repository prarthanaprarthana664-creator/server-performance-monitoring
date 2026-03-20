import streamlit as st
import pandas as pd

st.title("Server Performance Monitoring Dashboard")

# Load data safely
try:
    df = pd.read_excel("server_data.xlsx", engine="openpyxl")

    st.subheader("Dataset Preview")
    st.write(df.head())

    # CPU graph
    if "CPU_Utilization (%)" in df.columns:
        st.subheader("CPU Utilization")
        st.line_chart(df["CPU_Utilization (%)"])

    # Memory graph
    if "Memory_Usage (%)" in df.columns:
        st.subheader("Memory Usage")
        st.line_chart(df["Memory_Usage (%)"])

except Exception as e:
    st.error("Error loading dataset. Please check file format.")
