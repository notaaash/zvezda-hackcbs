import streamlit as st
from datetime import datetime
from features.routeFinder import load_station_data, find_route, get_junction_list
from features.get_train_btw_stations_page import get_trains_between_stations, check_availability, get_train_between_stations_page
from features.trains_between_stations import get_trains_between_stations
import pandas as pd

# Train Search Page
def train_search_page():
    st.title("Train Availability and Route Finder")

    # Input fields for the user
    from_station_code = st.text_input("From Station Code")
    to_station_code = st.text_input("To Station Code")
    date = st.date_input("Travel Date", min_value=datetime.today())

    # Convert date to string format if a date is selected
    formatted_date = date.strftime("%Y-%m-%d")

    # Load station data and junctions
    station_graph = load_station_data("mergedDataTrain.csv")
    junctions = get_junction_list()

    # Dropdown for selecting an intermediate junction
    intermediate_junction = st.selectbox("Select Intermediate Junction", ["None"] + junctions)

    # When the 'Search' button is clicked, invoke the search
    if st.button("Search Trains and Find Route", key="search_button"):
        if from_station_code and to_station_code:
            if intermediate_junction == "None":
                # Find direct route
                route = find_route(from_station_code, to_station_code, station_graph)
                if route:
                    display_route(route, junctions, from_station_code, to_station_code, formatted_date)
                else:
                    st.error("No route found between the specified stations.")
            else:
                # Find route in two legs
                route_leg1 = find_route(from_station_code, intermediate_junction, station_graph)
                route_leg2 = find_route(intermediate_junction, to_station_code, station_graph)
                if route_leg1 and route_leg2:
                    st.subheader("Route Found")
                    st.write("Leg 1:")
                    display_route(route_leg1, junctions, from_station_code, intermediate_junction, formatted_date, key_prefix="leg1_")
                    st.write("Leg 2:")
                    display_route(route_leg2, junctions, intermediate_junction, to_station_code, formatted_date, key_prefix="leg2_")
                else:
                    st.error("No route found for the specified legs.")
        else:
            st.error("Please enter both station codes.")

def display_route(route, junctions, from_station_code, to_station_code, date, key_prefix=""):
    route_html = "<div style='font-size: 18px; color: #4CAF50;'>"
    for station in route:
        if station in junctions:
            route_html += f"<span style='color: red; cursor: pointer;' onclick='handleJunctionClick(\"{station}\")'>{station}</span> <span style='font-size: 24px;'>&#10140;</span> "
        else:
            route_html += f"{station} <span style='font-size: 24px;'>&#10140;</span> "
    route_html = route_html.rstrip(" <span style='font-size: 24px;'>&#10140;</span> ")
    route_html += "</div>"
    st.markdown(route_html, unsafe_allow_html=True)
    st.markdown(f"""
        <script>
        function handleJunctionClick(station) {{
            const url = new URL(window.location.href);
            url.searchParams.set('junction', station);
            window.location.href = url.toString();
        }}
        </script>
    """, unsafe_allow_html=True)
    st.button("Book Tickets", key=f"{key_prefix}book_tickets", on_click=handle_book_tickets_click, args=(from_station_code, to_station_code, date))

def handle_book_tickets_click(from_station_code, to_station_code, date):
    st.write("Book Tickets button clicked")
    trains = get_trains_between_stations(from_station_code, to_station_code, date)
    if trains:
        train_data = trains['data']
        # Specify the fields to keep
        fields_to_keep = ['train_number', 'train_name', 'from_station_name', 'to_station_name', 'from_sta', 'to_sta', 'duration', 'train_type']
        filtered_data = [{field: train[field] for field in fields_to_keep} for train in train_data]
        df = pd.DataFrame(filtered_data)
        st.dataframe(df)
    else:
        st.error("No trains found for the specified route and date.")

# Function stub to handle junction click
def handle_junction_click(station):
    st.write(f"Junction clicked: {station}")

# Run the train search page
if __name__ == "__main__":
    train_search_page()