import streamlit as st
import pandas as pd

st.title("Server Performance Monitoring Dashboard")

df = pd.read_excel("server_data.xlsx")

st.subheader("Dataset Preview")
st.write(df.head())

if "CPU_Utilization (%)" in df.columns:
    st.subheader("CPU Utilization")
    st.line_chart(df["CPU_Utilization (%)"])

if "Memory_Usage (%)" in df.columns:
    st.subheader("Memory Usage")
    st.line_chart(df["Memory_Usage (%)"])
