from features.trains_between_stations import get_trains_between_stations
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("api_key.env")
api_key = os.getenv("RAPIDAPI_KEY")
api_host = os.getenv("RAPIDAPI_HOST")

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
        "quota": "GN",
        "trainNo": train["train_number"],
        "date": journey_date_str
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to retrieve availability. Status Code: {response.status_code}")
        return None

def get_train_between_stations_page():
    st.header("Get Train Between Stations")
    from_station = st.text_input("Enter Source Station Code:")
    to_station = st.text_input("Enter Destination Station Code:")
    journey_date = st.date_input("Select Date of Journey:")
    journey_date_str = str(journey_date)

    # Fetch trains on button click
    if st.button("Get Trains"):
        st.session_state["train_data"] = get_trains_between_stations(from_station, to_station, journey_date)
        st.session_state["from_station"] = from_station
        st.session_state["to_station"] = to_station
        st.session_state["journey_date_str"] = journey_date_str

    if "train_data" in st.session_state:
        data = st.session_state["train_data"]

        if data:
            for train in data['data']:
                st.subheader(f"Train Number: {train['train_number']} - {train['train_name']}")
                st.write(f"Source Station: {train['from_station_name']} ({train['train_src']})")
                st.write(f"Destination Station: {train['to_station_name']} ({train['train_dstn']})")
                st.write(f"Departure Time: {train['from_sta']} | Arrival Time: {train['to_sta']}")
                st.write(f"Duration: {train['duration']}")
                st.write(f"Train Type: {train['train_type']}")
                st.write(f"Classes Available: {', '.join(train['class_type'])}")
                st.write(f"Run Days: {', '.join(train['run_days'])}")
                st.write(f"Train Date: {train['train_date']}")
                st.write("---")

                # Create buttons for each class type
                for class_type in train['class_type']:
                    button_key = f"{train['train_number']}_{class_type}"
                    if st.button(f"Check Availability for {class_type}", key=button_key):
                        # Trigger availability check on button click
                        availability_data = check_availability(
                            class_type,
                            st.session_state["from_station"],
                            st.session_state["to_station"],
                            train,
                            st.session_state["journey_date_str"]
                        )

                        # Display availability if data is returned
                        if availability_data and availability_data.get("status"):
                            st.write("### Seat Availability Details")
                            for day_info in availability_data["data"]:
                                st.write(f"**Date**: {day_info['date']}")
                                st.write(f"- **Ticket Fare**: ₹{day_info['ticket_fare']}")
                                st.write(
                                    f"- **Confirm Probability**: {day_info['confirm_probability']} ({day_info['confirm_probability_percent']}%)")
                                st.write(f"- **Current Status**: {day_info['current_status']}")
                                st.write("---")
                        else:
                            st.warning("No availability information returned from the API.")
        else:
            st.error("No trains found or error in fetching data. Please try again.")
    else:
        st.warning("Please fill all the fields and click 'Get Trains'.")
