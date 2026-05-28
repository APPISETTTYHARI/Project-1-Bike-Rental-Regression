`import streamlit as st
import joblib
import numpy as np

model = joblib.load("bike_model.pkl")

st.title("🚲 Bike Demand Prediction")

st.subheader("Weather Inputs")
temp = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 50.0)
windspeed = st.slider("Wind Speed", 0.0, 50.0, 10.0)
weather = st.selectbox("Weather Condition", [1,2,3,4])

st.subheader("Time & Context Inputs")
season = st.selectbox("Season", [1,2,3,4])
month = st.slider("Month", 1, 12, 6)
day_of_week = st.slider("Day of Week (0=Sun,6=Sat)", 0, 6, 3)
hour = st.slider("Hour of Day", 0, 23, 12)
holiday = st.selectbox("Holiday (0=No,1=Yes)", [0,1])
workingday = st.selectbox("Working Day (0=No,1=Yes)", [0,1])

if st.button("Predict Demand"):
    
    input_data = np.array([[
        temp,
        humidity,
        windspeed,
        weather,
        season,
        month,
        day_of_week,
        hour,
        holiday,
        workingday
    ]])
    
    prediction = model.predict(input_data)[0]
    
    st.metric("Predicted Bike Count", f"{int(prediction)} bikes")

