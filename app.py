import streamlit as st

# Set up the Streamlit app title
st.title("Taxi Fare Model")

# Ask the user for input parameters
st.sidebar.header("Input Parameters")

# Input for pickup longitude and latitude
pickup_longitude = st.sidebar.number_input("Pickup Longitude", min_value=-180.0, max_value=180.0, step=0.001, value=0.0)
pickup_latitude = st.sidebar.number_input("Pickup Latitude", min_value=-90.0, max_value=90.0, step=0.001, value=0.0)

# Input for dropoff longitude and latitude
dropoff_longitude = st.sidebar.number_input("Dropoff Longitude", min_value=-180.0, max_value=180.0, step=0.001, value=0.0)
dropoff_latitude = st.sidebar.number_input("Dropoff Latitude", min_value=-90.0, max_value=90.0, step=0.001, value=0.0)

# Input for passenger count
passenger_count = st.sidebar.number_input("Passenger Count", min_value=1, value=1)

if st.sidebar.button("Calculate Fare Prediction"):
    # You can add the code here to calculate the prediction without making an API call
    # Make sure to validate user inputs and perform the prediction
    # For demonstration purposes, let's calculate a simple prediction based on user inputs
    base_fare = 5.0
    fare_per_mile = 2.0
    prediction = base_fare + fare_per_mile * pickup_latitude

    st.sidebar.success(f"The estimated fare is ${prediction:.2f}")
