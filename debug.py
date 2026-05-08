myMap = {
    "nodes": 
        [(6734.0, 1453.0), (2233.0, 10.0), (5530.0, 1424.0), (401.0, 841.0), (3082.0, 1644.0)],
    "euclid_distances":
        [[0.0, 4726.653149957166, 1204.3492018513568, 6362.502102160753, 3656.991249647721],
        [4726.653149957166, 0.0, 3587.4231699090087, 2011.6622479929379, 1841.400825458705],
        [1204.3492018513568, 3587.4231699090087, 0.0, 5162.02770236658, 2457.865740841025],
        [6362.502102160753, 2011.6622479929379, 5162.02770236658, 0.0, 2798.672899786611],
        [3656.991249647721, 1841.400825458705, 2457.865740841025, 2798.672899786611, 0.0]]
}

visited = [False] * len(myMap["nodes"])
nn_distance = 0
tour_list = []

# Initiating
start = 0
visited[start] = True
tour_list.append(start)
current = start

for i in range(len(myMap["euclid_distances"])-1):
    shortest_distance = float("inf")
    nearest_index = current
    for i in range(len(myMap["euclid_distances"][current])):
        if myMap["euclid_distances"][current][i] < shortest_distance and not (myMap["euclid_distances"][current][i] == 0):
            shortest_distance = myMap["euclid_distances"][current][i]
            nearest_index = i
            
    print(shortest_distance, nearest_index)
    nn_distance += shortest_distance
    current = nearest_index
    visited[current] = True
    tour_list.append(current)
    
print(nn_distance)