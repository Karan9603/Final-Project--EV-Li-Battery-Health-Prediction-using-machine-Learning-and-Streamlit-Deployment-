import streamlit as st
import joblib
import numpy as np


# Load the trained model
model = joblib.load("battery_health_L_model.joblib")

# Streamlit App
st.title("🔋 Battery Health Prediction App")
st.write("Enter the required details to predict battery health.")


#  5   Charging Mode_Normal             1000 non-null   int64  
#  6   Charging Mode_Slow               1000 non-null   int64  
#  7   attery Type_LiFePO4             1000 non-null   int64  
#  8   EV Model_Model B                 1000 non-null   int64  
#  9   EV Model_Model C                 1000 non-null   int64  

# User Inputs
soc = st.number_input("SOC (%)", min_value=0.0, max_value=100.0, step=0.1)
battery_temp = st.number_input("Battery Temperature (°C)", min_value=-10.0, max_value=100.0, step=0.1)
charging_duration = st.number_input("Charging Duration (min)", min_value=0, max_value=1000, step=1)
Optimal_Charging_Duration_Class = st.number_input("Optimal Charging Duration Class", min_value=0, max_value=2, step=1)

Charging_Mode_Normal = st.number_input("Charging Mode_Normal", min_value=-0, max_value=1, step=1)
Charging_Mode_Slow = st.number_input("Charging Mode_Slow", min_value=-0, max_value=1, step=1)
Battery_Type_LiFePO4 = st.number_input("Battery Type_LiFePO4", min_value=-0, max_value=1, step=1)
EV_Model_Model_B = st.number_input("EV Model_Model B", min_value=-0, max_value=1, step=1)
EV_Model_Model_C = st.number_input("EV Model_Model C", min_value=-0, max_value=1, step=1)

# voltage = st.number_input("Voltage (V)", min_value=0.0, max_value=500.0, step=0.1)
# charging_cycles = st.number_input("Charging Cycles", min_value=0, max_value=10000, step=1)

# Add more inputs based on your dataset

# Prediction Button
if st.button("Predict Battery Health"):
    # Prepare input data
    input_data = np.array([[soc, battery_temp, charging_duration, Optimal_Charging_Duration_Class, Charging_Mode_Normal, Charging_Mode_Slow, Battery_Type_LiFePO4, EV_Model_Model_B, EV_Model_Model_C ]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.success(f"🔋 Predicted Battery Health: {prediction:.2f}")