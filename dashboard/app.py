# dashboard/app.py
import streamlit as st
import requests

backend_url = "http://backend:8000"

st.title("Battery Analytics Dashboard")

# Simulate new battery
st.header("Run Simulation")
battery_model = st.selectbox("Battery Model", ["DFN", "SPM"])
parameters = st.text_area("Simulation Parameters (JSON)")
if st.button("Run Simulation"):
    response = requests.post(f"{backend_url}/simulate", json={
        "battery_model": battery_model,
        "parameters": eval(parameters)
    })
    st.write(response.json())

# View insights
st.header("Simulation Insights")
response = requests.get(f"{backend_url}/results")
insights = response.json()
st.write(insights)
for insight in insights:
    st.line_chart(insight["metrics"])
