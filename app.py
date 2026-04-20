import streamlit as st
import pandas as pd
from model import predict_energy

st.set_page_config(page_title="UrbanIQ", layout="centered")

st.title("UrbanIQ - Smart City AI")

st.sidebar.header("Control Panel")
traffic = st.sidebar.slider("Traffic Level", 50, 200, 100)

# Prediction
result = predict_energy(traffic)

st.subheader("AI Prediction")
st.write(f"Estimated Energy Usage: {result}")

# Recommendation
if traffic > 150:
    st.warning("High traffic detected! Suggestion: Optimize traffic lights 🚦")
else:
    st.success("Traffic is stable ✅")

# Load data for chart
df = pd.read_csv("data.csv")

st.subheader("Traffic vs Energy Data")
st.line_chart(df)
