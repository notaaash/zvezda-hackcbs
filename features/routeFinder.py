import csv
from collections import defaultdict, deque
import os

# Get the current working directory
current_directory = os.getcwd()

# Construct the full path to the file
file_path = os.path.join(current_directory, 'utils', 'merged-data-train.csv')


# Step 1: Load the file and create the graph
def load_station_data(file_path):
    station_graph = defaultdict(list)

    with open(file_path, mode='r') as file:
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


# Step 2: Implement the route-finding logic using BFS
def find_route(start, end, station_graph):
    # Direct route if it exists (bidirectional check)
    if end in station_graph[start]:
        return [start, end]

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


# Step 3: Test the code
 # Path to your station file
station_graph = load_station_data(file_path)

start_station = "A"
end_station = "G"
route = find_route(start_station, end_station, station_graph)

if route:
    print(f"Route found from {start_station} to {end_station}: {' -> '.join(route)}")
else:
    print(f"No route found from {start_station} to {end_station}")
