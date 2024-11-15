import csv
from collections import defaultdict, deque
import os

# Get the current working directory
current_directory = os.getcwd()

# Construct the full path to the file
file_path = os.path.join(current_directory, "mergedDataTrain.csv")

# Step 1: Load the file and create the graph
def load_station_data(merged_data_train):
    station_graph = defaultdict(list)

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            station = row[0]  # The first column is the station code
            next_stations = row[1:]  # The remaining columns are the next station codes

            # Add the current station and its next stations to the graph
            station_graph[station].extend(next_stations)

            # For bidirectional routes, ensure reverse connections as well
            for next_station in next_stations:
                station_graph[next_station].append(station)

    return station_graph

# Step 2: Identify junctions
def find_junctions(station_graph):
    junctions = [station for station, connections in station_graph.items() if len(connections) >= 6]
    return junctions

# Step 3: Implement the route-finding logic using BFS
def find_route(start, end, station_graph):
    # Use BFS to find paths through junctions
    queue = deque([(start, [start])])  # Each element is (current_station, path_so_far)
    visited = set([start])  # Keep track of visited stations to avoid cycles

    while queue:
        current_station, path = queue.popleft()

        # Iterate through each next station
        for next_station in station_graph[current_station]:
            # Check if we've reached the destination
            if next_station == end:
                return path + [end]

            # Check if next_station is unvisited
            if next_station not in visited:
                visited.add(next_station)
                queue.append((next_station, path + [next_station]))

    # If no route is found
    return None

# Step 4: Test the code
# Path to your station file
station_graph = load_station_data(file_path)

def get_junction_list():
    return junctions

# Find junctions
junctions = find_junctions(station_graph)
print(f"Junctions: {junctions}")

# Test route finding
start_station = "RKMP"
end_station = "NZM"
route = find_route(start_station, end_station, station_graph)

if route:
    print(f"Route found from {start_station} to {end_station}: {' -> '.join(route)}")
else:
    print(f"No route found from {start_station} to {end_station}")