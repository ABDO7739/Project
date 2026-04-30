campus_graph = {
    "Entrance": {"Administration": 4, "Dorms": 5},
    "Administration": {"Entrance": 4, "Library": 6, "Student center": 5, "Lecture 1 Hall": 2},
    "Library": {"Administration": 6, "Lecture 3 Hall": 3, "Student center": 2, "Lab 1": 4},
    "Lecture 3 Hall": {"Library": 3, "Lab 1": 2, "Student Affairs Office": 5, "Electronics Lab": 9},
    "Student center": {"Administration": 5, "Library": 2, "Lab 1": 1, "Lecture 1 Hall": 4, "Parking": 8},
    "Lab 1": {"Student center": 1, "Library": 4, "Lecture 3 Hall": 2, "Student Affairs Office": 7},
    "Lecture 1 Hall": {"Administration": 2, "Student center": 4, "Dorms": 3, "Parking": 4},
    "Dorms": {"Entrance": 5, "Lecture 1 Hall": 3, "Parking": 7, "Lecture 2 Hall": 3},
    "Parking": {"Lecture 1 Hall": 4, "Dorms": 7, "Lecture 2 Hall": 9, "Gym": 11, "Student center": 8},
    "Lecture 2 Hall": {"Dorms": 3, "Parking": 9, "Lab 2": 5},
    "Gym": {"Parking": 11, "Lab 2": 8, "Student Affairs Office": 6},
    "Lab 2": {"Lecture 2 Hall": 5, "Gym": 8, "Physics laboratory": 12},
    "Student Affairs Office": {"Lab 1": 7, "Lecture 3 Hall": 5, "Gym": 6, "Physics laboratory": 4, "Electronics Lab": 8},
    "Physics laboratory": {"Student Affairs Office": 4, "Lab 2": 12, "IT": 10},
    "Electronics Lab": {"Lecture 3 Hall": 9, "Student Affairs Office": 8, "IT": 11},
    "IT": {"Physics laboratory": 10, "Electronics Lab": 11},
}
def bfs(start , goal):
    visited = []
    fronter = [(start,[start])]
    while len(fronter)>0:
        curr_city, curr_path = fronter.pop(0)
        if curr_city == goal:
            return  curr_path
        if curr_city not in visited:
           visited.append(curr_city)
           neighboors = graph[curr_city] 
           for city , cost in neighboors:
               fronter .append((city,curr_path+[city]))
    return "No solution found!"

sol = bfs("Entrance" ,"IT")
#BFS algorithm
def uniform_cost2(start,goal):
    visited = []
    fronter = [(0,start,[start])]
    while len(fronter) > 0:
        fronter.sort()
        curr_cost, curr_city, curr_path = fronter.pop(0)
        if curr_city == goal:
            return (curr_path, curr_cost)
        if curr_city not in visited:
            visited.append(curr_city)
            for child_city, child_cost in graph[curr_city]:
                fronter.append((
                    curr_cost + child_cost,
                    child_city,
                    curr_path + [curr_city]
                ))
                return"No Solution found!"
            sol,cost = uniform_cost2("Entrance","IT")
            print(f"{sol}\nTotal cost = {cost}")

