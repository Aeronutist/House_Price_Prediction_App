import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Page title
st.title("🏡 House Price Prediction App")
st.markdown("Enter the details below to predict the house price.")

# Input fields
longitude = st.number_input("Longitude", value=-120.0)
latitude = st.number_input("Latitude", value=37.0)
housing_median_age = st.slider("Housing Median Age", 1, 100, 25)
total_rooms = st.number_input("Total Rooms", value=2000)
total_bedrooms = st.number_input("Total Bedrooms", value=400)
population = st.number_input("Population", value=1000)
households = st.number_input("Households", value=300)
median_income = st.number_input("Median Income (in 1000s)", value=4.0)

# Ocean proximity options (One-hot encoded)
ocean_options = ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']
selected = st.selectbox("Ocean Proximity", ocean_options)

# Map selection to one-hot encoding (drop_first=True was used)
ocean_dict = {
    '<1H OCEAN': [0,0,0,0],
    'INLAND':    [1,0,0,0],
    'ISLAND':    [0,1,0,0],
    'NEAR BAY':  [0,0,1,0],
    'NEAR OCEAN':[0,0,0,1]
}

# Create input array
features = np.array([
    longitude, latitude, housing_median_age,
    total_rooms, total_bedrooms, population,
    households, median_income,
    *ocean_dict[selected]
]).reshape(1, -1)

# Scale inputs
scaled_features = scaler.transform(features)

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(scaled_features)[0]
    st.success(f"predicted house price : Rs. {int(prediction):,}")
    