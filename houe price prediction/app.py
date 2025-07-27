
import streamlit as st
import numpy as np
import pickle

# Load the model
model = pickle.load(open('linear_regression_model.pkl', 'rb'))

st.title("🏠 USA Housing Price Prediction App")
st.write("Enter the values below to predict the house price:")

# Input fields
income = st.number_input("Average Area Income", value=60000.0)
age = st.number_input("Average Area House Age", value=5.0)
rooms = st.number_input("Average Area Number of Rooms", value=7.0)
bedrooms = st.number_input("Average Area Number of Bedrooms", value=4.0)
population = st.number_input("Area Population", value=30000.0)

if st.button("Predict Price"):
    input_data = np.array([[income, age, rooms, bedrooms, population]])
    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Predicted House Price: ${prediction:,.2f}")
