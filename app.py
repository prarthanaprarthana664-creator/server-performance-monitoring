import pandas as pd
import streamlit as st

st.title("Virtual Server Monitoring Dashboard")

# safe file loading
try:
    file_path = "server_data.xlsx"
    metadata = pd.read_excel(file_path, sheet_name="Server_Metadata", engine="openpyxl")
    s1 = pd.read_excel(file_path, sheet_name="Server_Performance_Station1", engine="openpyxl")
    s2 = pd.read_excel(file_path, sheet_name="Server_Performance_Station2", engine="openpyxl")

    df = pd.concat([s1, s2])

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("CPU Utilization Trend")
    st.line_chart(df["CPU_Utilization (%)"])

    st.subheader("Memory Usage Trend")
    st.line_chart(df["Memory_Usage (%)"])

    st.metric("Average CPU Usage", round(df["CPU_Utilization (%)"].mean(), 2))

except Exception as e:
    st.error(f"Error loading file: {e}")
