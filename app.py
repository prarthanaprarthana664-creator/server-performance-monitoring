import streamlit as st
import pandas as pd
import numpy as np

st.title("Server Performance Monitoring Dashboard")

# generate sample data (no file dependency)
data = pd.DataFrame({
    "CPU_Utilization (%)": np.random.randint(20, 100, 100),
    "Memory_Usage (%)": np.random.randint(30, 90, 100)
})

st.subheader("Dataset Preview")
st.write(data.head())

st.subheader("CPU Utilization Trend")
st.line_chart(data["CPU_Utilization (%)"])

st.subheader("Memory Usage Trend")
st.line_chart(data["Memory_Usage (%)"])

st.metric("Average CPU Usage", round(data["CPU_Utilization (%)"].mean(), 2))
