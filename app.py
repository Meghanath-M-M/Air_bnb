import streamlit as st
import pandas as pd
import joblib

model = joblib.load("airbnb_price_pipeline.pkl")

st.title("🏠 Airbnb Nightly Price Predictor")

st.write(
    "Predict the estimated nightly rental price of an Airbnb property in New York City."
)

neighbourhood_group = st.selectbox(
    "Neighbourhood Group", ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
)

neighbourhood = st.text_input("Neighbourhood", "Harlem")

latitude = st.number_input("Latitude", value=40.81)

longitude = st.number_input("Longitude", value=-73.94)

room_type = st.selectbox(
    "Room Type", ["Private room", "Entire home/apt", "Shared room"]
)

minimum_nights = st.number_input("Minimum Nights", min_value=1, value=2)

number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=25)

reviews_per_month = st.number_input("Reviews per Month", min_value=0.0, value=1.2)

calculated_host_listings_count = st.number_input(
    "Host Listings Count", min_value=1, value=2
)

availability_365 = st.number_input(
    "Availability (365 days)", min_value=0, max_value=365, value=200
)

if st.button("Predict Price"):
    input_data = pd.DataFrame(
        {
            "neighbourhood_group": [neighbourhood_group],
            "neighbourhood": [neighbourhood],
            "latitude": [latitude],
            "longitude": [longitude],
            "room_type": [room_type],
            "minimum_nights": [minimum_nights],
            "number_of_reviews": [number_of_reviews],
            "reviews_per_month": [reviews_per_month],
            "calculated_host_listings_count": [calculated_host_listings_count],
            "availability_365": [availability_365],
        }
    )

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated nightly price: ${prediction:.2f}")
