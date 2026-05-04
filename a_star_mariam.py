graph = {
    'Entrance': [('Administration', 4), ('Dorms', 5)],
    'Administration': [('Entrance', 4), ('Library', 6), ('Lecture 1 Hall', 2), ('Student center', 5)],
    'Dorms': [('Entrance', 5), ('Lecture 1 Hall', 3), ('Parking', 7), ('Lecture 2 Hall', 3)],
    'Library': [('Administration', 6), ('Student center', 2), ('Lab 1', 4), ('Lecture 3 Hall', 3)],
    'Lecture 1 Hall': [('Administration', 2), ('Dorms', 3), ('Student center', 4)],
    'Student center': [('Administration', 5), ('Library', 2), ('Lecture 1 Hall', 4), ('Lab 1', 1), ('Parking', 8)],
    'Parking': [('Dorms', 7), ('Student center', 8), ('Gym', 11)],
    'Lecture 2 Hall': [('Dorms', 3), ('Parking', 9), ('Lab 2', 5)],
    'Lab 1': [('Library', 4), ('Student center', 1), ('Lecture 3 Hall', 2), ('Student Affairs Office', 7)],
    'Lecture 3 Hall': [('Library', 3), ('Lab 1', 2), ('Electronics Lab', 9)],
    'Gym': [('Parking', 11), ('Student Affairs Office', 6), ('Lab 2', 8)],
    'Lab 2': [('Lecture 2 Hall', 5), ('Gym', 8), ('Physics laboratory', 12)],
    'Student Affairs Office': [('Lab 1', 7), ('Gym', 6), ('Electronics Lab', 8), ('Physics laboratory', 4)],
    'Physics laboratory': [('Lab 2', 12), ('Student Affairs Office', 4), ('Electronics Lab', 10)],
    'Electronics Lab': [('Lecture 3 Hall', 9), ('Student Affairs Office', 8), ('Physics laboratory', 10), ('IT', 11)],
    'IT': [('Electronics Lab', 11)]
}
heuristic = {
    'Entrance': 18,
    'Administration': 16,
    'Dorms': 19,
    'Library': 13,
    'Lecture 1 Hall': 17,
    'Student center': 12,
    'Parking': 15,
    'Lecture 2 Hall': 20,
    'Lab 1': 11,
    'Lecture 3 Hall': 9,
    'Gym': 10,
    'Lab 2': 14,
    'Student Affairs Office': 7,
    'Physics laboratory': 5,
    'Electronics Lab': 3,
    'IT': 0
}


def A_star(start , end ): 
    visited = []
    fronteer = [(0 + heuristic[start] , start , [start ])]
    while len(fronteer)> 0:
        fronteer.sort()
        curr_cost , curr_campus , curr_path = fronteer.pop(0)
        curr_actaul_cost= curr_cost - heuristic[curr_campus] 
        if curr_campus == end:
            return curr_path , curr_actaul_cost
        if curr_campus not in visited:
            visited.append(curr_campus) 
            neigboor = graph[curr_campus]
            for child_campus , child_cost in neigboor:
                
                   fronteer.append((child_cost + heuristic[child_campus] + curr_actaul_cost , child_campus , curr_path+[child_campus]))
    

          
    return "no slution found !"

sol, cost = A_star("Entrance" , "IT")
print (f"the path to goal is {sol} and the cost to the path is {cost}")