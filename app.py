import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("energy_forecast_xgboost.pkl")

st.title("Energy Consumption Forecast")

st.write("Enter time and previous consumption values:")

hour = st.slider("Hour", 0, 23, 12)
dayofweek = st.slider("Day of Week (0=Mon)", 0, 6, 3)
month = st.slider("Month", 1, 12, 6)
year = st.number_input("Year", value=2015)

lag_1 = st.number_input("Consumption 1 hour ago")
lag_24 = st.number_input("Consumption 24 hours ago")
lag_168 = st.number_input("Consumption 1 week ago")

if st.button("Predict"):
    features = np.array([[hour, dayofweek, month, year, lag_1, lag_24, lag_168]])
    prediction = model.predict(features)[0]

    st.success(f"Predicted Energy Consumption: {prediction:.2f} MW")


