from features.trains_between_stations import get_trains_between_stations
from features.get_train_btw_stations_page import get_train_between_stations_page
import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from features.searchAlternate import train_search_page

# # Example of calling the function in app.py
# # Streamlit UI for user input
# st.title("Trains Between Stations")
#
# # Input fields for the user
# from_station = st.text_input("Enter Source Station Code:")
# to_station = st.text_input("Enter Destination Station Code:")
# journey_date = st.date_input("Select Date of Journey:")
#
# # Button to fetch the trains when clicked
# if st.button("Find Trains"):
#     if from_station and to_station and journey_date:
#         # Display the data being passed before sending the request
#         journey_date_str = str(journey_date)  # Convert to string for visual clarity
#
#         # Debugging: Show what is being passed
#         st.write(f"Date being passed to the API: {journey_date_str}")
#
#         # Fetch train data from the API
#         data = get_trains_between_stations(from_station, to_station, journey_date)
#
#         if data:
#             for train in data['data']:
#                 st.subheader(f"Train Number: {train['train_number']} - {train['train_name']}")
#                 st.write(f"Source Station: {train['from_station_name']} ({train['train_src']})")
#                 st.write(f"Destination Station: {train['to_station_name']} ({train['train_dstn']})")
#                 st.write(f"Departure Time: {train['from_sta']} | Arrival Time: {train['to_sta']}")
#                 st.write(f"Duration: {train['duration']}")
#                 st.write(f"Train Type: {train['train_type']}")
#                 st.write(f"Classes Available: {', '.join(train['class_type'])}")
#                 st.write(f"Run Days: {', '.join(train['run_days'])}")
#                 st.write(f"Train Date: {train['train_date']}")
#                 st.write("---")
#         else:
#             st.error("No trains found or error in fetching data. Please try again.")
#     else:
#         st.warning("Please fill all the fields.")


# Function for "Get Train Between Stations"


# Function for "Get Live Train Status"
def get_live_train_status():
    st.header("Get Live Train Status")
    train_number = st.text_input("Enter Train Number:")
    if st.button("Get Live Status"):
        # Logic to fetch live train status
        st.write(f"Fetching live status for Train {train_number}...")
        # Example live status (replace with real API calls or logic)
        st.write("Train 12345 is running on time.")

# Function for "Get PNR Status"
def get_pnr_status():
    st.header("Get PNR Status")
    pnr_number = st.text_input("Enter PNR Number:")
    if st.button("Check PNR Status"):
        # Logic to fetch PNR status
        st.write(f"Fetching PNR status for {pnr_number}...")
        # Example PNR status (replace with real API calls or logic)
        st.write("Your PNR is confirmed. Seat: 10A")

def search_alternate():
    train_search_page()

# Main App Logic
def main():
    st.title("zvezda portal")

    # Sidebar navigation
    page = st.sidebar.radio("Choose a feature", ["Home", "Get Train Between Stations", "Get Live Train Status", "Get PNR Status", "Search Alternate Routes"])

    # Display the content based on the selected page
    if page == "Home":
        st.header("Welcome to the Train Information Portal")
        st.write("Select a feature from the sidebar to get started.")
    elif page == "Get Train Between Stations":
        get_train_between_stations_page()
    elif page == "Get Live Train Status":
        get_live_train_status()
    elif page == "Get PNR Status":
        get_pnr_status()
    elif page == "Search Alternate Routes":
        train_search_page()

# Run the app
if __name__ == "__main__":
    main()
