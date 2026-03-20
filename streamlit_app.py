import streamlit as st
import pandas as pd

st.title("Server Monitoring Dashboard")

try:
    df = pd.read_excel("server_data.xlsx")

    st.write(df.head())

    if "CPU_Utilization (%)" in df.columns:
        st.line_chart(df["CPU_Utilization (%)"])

    if "Memory_Usage (%)" in df.columns:
        st.line_chart(df["Memory_Usage (%)"])

except Exception as e:
    st.error(e)
