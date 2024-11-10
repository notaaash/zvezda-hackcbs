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
    st.logo('./utils/imagebg.jpg', size="large", link=None, icon_image='./utils/imagebg.jpg')
    st.title("zvezda portal")
    st.header("<- please select the appropriate option from the sidebar")
    tiger_ascii = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠋⠁⠀⠀⠀⠈⠙⢦⣄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠑⢤⣀⠉⠙⠓⢦⣀⠀⠀⠀⠀⠀⠈⠻⣄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⢦⣄⠈⠙⢦⡀⠀⠀⠀⠀⠈⠳
    ⠀⠀⠀⢀⣀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣄⠙⢦⡀⠀⠀⠀⠀
    ⠀⠀⠀⠸⢿⣧⡈⠙⠳⢦⣤⣤⣄⡀⠀⠀⠀⠉⠙⢦⡙⢦⠀⠀⠀
    ⠀⠀⠀⠀⠀⠉⠙⠓⠶⢬⠽⢿⣻⣿⣦⣄⡀⠀⠀⠀⠙⠳⢧⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣈⠙⢿⣿⣿⣶⣤⣄⣀⣀⠙⢦
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⠳⢦⣍⠙⠿⢿⣿⣿⣿⣷⣄
    ⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠙⠛⠿⠶⣤⣤⣉⠙⢦⣀⠀⠙⢿⣿⣿
    ⠀⠀⠀⠀⠀⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⢦⣙⠳⠶⠤⢌⣛
    ⠀⠀⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⣀⣀⣼⣿
    ⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⢻⣿
    """

    # Display the ASCII art with monospaced formatting
    st.markdown(tiger_ascii)
    # st.image('./utils/imagebg.jpg')

    st.sidebar.title("Train Information System")
    st.sidebar.markdown("""
        <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
            padding: 20px;
        }
        .sidebar .sidebar-content h1 {
            color: #4CAF50;
        }
        .sidebar .sidebar-content p {
            color: #333;
        }
        .sidebar .sidebar-content .button {
            display: block;
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            font-size: 18px;
            text-align: center;
            color: white;
            background-color: #4CAF50;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .sidebar .sidebar-content .button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.header("Navigation")
    if st.sidebar.button("Get Train Between Stations", key="get_train_between_stations"):
        get_train_between_stations_page()
    if st.sidebar.button("Get Live Train Status", key="get_live_train_status"):
        get_live_train_status()
    if st.sidebar.button("Get PNR Status", key="get_pnr_status"):
        get_pnr_status()
    if st.sidebar.button("Search Alternate Routes", key="search_alternate_routes"):
        train_search_page()

# Run the app
if __name__ == "__main__":
    main()
