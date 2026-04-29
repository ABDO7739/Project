graph = {
    "Porta Nuova":                [("KFC Milano Duomo", 5)],
    "KFC Milano Duomo":           [("Porta Nuova", 5), ("Milano Centrale Station", 3), ("Navigli", 4)],
    "Navigli":                    [("KFC Milano Duomo", 4)],
    "Milano Centrale Station":    [("KFC Milano Duomo", 3), ("Torino Porta Susa", 140), ("Bologna Centrale", 215)],
    "Torino Porta Susa":          [("Milano Centrale Station", 140), ("Verona Porta Nuova", 280)],
    "Verona Porta Nuova":         [("Torino Porta Susa", 280), ("Bologna Centrale", 145)],
    "Bologna Centrale":           [("Milano Centrale Station", 215), ("Verona Porta Nuova", 145), ("Roma Termini Station", 375), ("Firenze Santa Maria Novella", 110)],
    "Roma Termini Station":       [("Bologna Centrale", 375), ("McDonald's Roma Termini", 2), ("Napoli Centrale Station", 445)],
    "McDonald's Roma Termini":    [("Roma Termini Station", 2), ("Trastevere", 8), ("EUR District", 5)],
    "Trastevere":                 [("McDonald's Roma Termini", 8)],
    "EUR District":               [("McDonald's Roma Termini", 5)],
    "Firenze Santa Maria Novella":[("Bologna Centrale", 110), ("Subway Firenze Centro", 44)],
    "Subway Firenze Centro":      [("Firenze Santa Maria Novella", 44), ("Oltrarno", 31), ("Pisa Centrale", 25), ("Campo di Marte", 112)],
    "Oltrarno":                   [("Subway Firenze Centro", 31)],
    "Pisa Centrale":              [("Subway Firenze Centro", 25), ("Burger King Napoli Centrale", 78)],
    "Campo di Marte":             [("Subway Firenze Centro", 112)],
    "Burger King Napoli Centrale":[("Pisa Centrale", 78), ("Napoli Centrale Station", 56), ("Vomero", 15)],
    "Napoli Centrale Station":    [("Roma Termini Station", 445), ("Burger King Napoli Centrale", 56)],
    "Vomero":                     [("Burger King Napoli Centrale", 15), ("Posillipo", 19)],
    "Posillipo":                  [("Vomero", 19)]
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

sol = bfs("Milano Centrale Station" , "Posillipo")
