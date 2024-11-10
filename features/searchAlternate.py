import streamlit as st
from datetime import datetime
from features.routeFinder import load_station_data, find_route, get_junction_list

# Train Search Page
def train_search_page():
    st.title("Train Availability and Route Finder")

    # Input fields for the user
    from_station_code = st.text_input("From Station Code")
    to_station_code = st.text_input("To Station Code")
    date = st.date_input("Travel Date", min_value=datetime.today())

    # Convert date to string format if a date is selected
    formatted_date = date.strftime("%Y-%m-%d")

    # When the 'Search' button is clicked, invoke the search
    if st.button("Search Trains and Find Route"):
        if from_station_code and to_station_code:
            # Load station data and find the route
            station_graph = load_station_data("mergedDataTrain.csv")
            route = find_route(from_station_code, to_station_code, station_graph)
            junctions = get_junction_list()

            if route:
                st.subheader("Route Found")
                route_html = "<div style='font-size: 18px; color: #4CAF50;'>"
                for station in route:
                    if station in junctions:
                        route_html += f"<span style='color: red;'>{station}</span> <span style='font-size: 24px;'>&#10140;</span> "
                    else:
                        route_html += f"{station} <span style='font-size: 24px;'>&#10140;</span> "
                route_html = route_html.rstrip(" <span style='font-size: 24px;'>&#10140;</span> ")
                route_html += "</div>"
                st.markdown(route_html, unsafe_allow_html=True)
            else:
                st.error("No route found between the specified stations.")
        else:
            st.error("Please enter both station codes.")