import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load the environment variables from the .env file
load_dotenv("api_key.env")

# Get the API key and host from environment variables
api_key = os.getenv("RAPIDAPI_KEY")
api_host = os.getenv("RAPIDAPI_HOST")


# Function to fetch trains data from API
def check_availability(class_type, from_station, to_station, train, journey_date_str):
    url = f"https://{api_host}/api/v1/checkSeatAvailability"
    headers = {
        "x-rapidapi-host": api_host,
        "x-rapidapi-key": api_key
    }
    params = {
        "classType": class_type,
        "fromStationCode": from_station,
        "toStationCode": to_station,
        "quota": "GN",  # Assuming "GN" (General Quota) here, adjust as needed
        "trainNo": train["train_number"],
        "dateOfJourney": journey_date_str
    }

    # Debugging: Show what data is being sent
    st.text(f"Sending request with the following parameters:\n"
            f"From Station: {from_station}\n"
            f"To Station: {to_station}\n"
            f"Journey Date: {journey_date_str}")

    response = requests.get(url, headers=headers, params=params)
    return response.json() if response.status_code == 200 else None
