import streamlit as st
from data_processing import load_data, transform_data

st.title("Virtual Server Monitoring Dashboard")

file_path = file_path = "server_data.xlsx"

# load data
metadata, s1, s2 = load_data(file_path)

# transform data
server_data = transform_data(metadata, s1, s2)

# show data
st.subheader("Dataset Preview")
st.write(server_data.head())

# CPU graph
st.subheader("CPU Utilization Trend")
st.line_chart(server_data["CPU_Utilization (%)"])

# Memory graph
st.subheader("Memory Usage Trend")
st.line_chart(server_data["Memory_Usage (%)"])

# KPI
st.metric("Average CPU Usage", round(server_data["CPU_Utilization (%)"].mean(), 2))
