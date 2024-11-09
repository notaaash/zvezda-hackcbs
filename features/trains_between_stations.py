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
def get_trains_between_stations(from_station, to_station, date_of_journey):
    url = f"https://{api_host}/api/v3/trainBetweenStations"
    headers = {
        "x-rapidapi-host": api_host,
        "x-rapidapi-key": api_key
    }
    params = {
        'fromStationCode': from_station,
        'toStationCode': to_station,
        'dateOfJourney': date_of_journey  # Send the date object directly
    }

    # Debugging: Show what data is being sent
    st.text(f"Sending request with the following parameters:\n"
            f"From Station: {from_station}\n"
            f"To Station: {to_station}\n"
            f"Journey Date: {date_of_journey}")

    response = requests.get(url, headers=headers, params=params)
    return response.json() if response.status_code == 200 else None