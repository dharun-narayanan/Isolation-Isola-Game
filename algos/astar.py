#astar search algorithm
def astar (start, goal, neighbors):
    #initialize the open and closed lists
    open_list = []
    closed_list = []
    #initialize the open list with the start node
    open_list.append(start)
    #loop until the open list is empty
    while len(open_list) > 0:
        #find the node in the open list with the lowest f value
        current = open_list[0]
        for node in open_list:
            if node.f < current.f:
                current = node
        #remove the current node from the open list and add it to the closed list
        open_list.remove(current)
        closed_list.append(current)
        #if the current node is the goal node, return the path
        if current == goal:
            path = []
            while current in closed_list:
                path.append(current)
                current = current.parent
            return path[::-1]
        #generate the neighbors of the current node
        neighbors = neighbors(current)
        #loop through the neighbors
        for neighbor in neighbors:
            #if the neighbor is already in the closed list, skip it
            if neighbor in closed_list:
                continue
            #set the neighbor's parent to the current node
            neighbor.parent = current
            #calculate the g and h values of the neighbor
            neighbor.g = current.g + neighbor.cost
            neighbor.h = neighbor.heuristic(goal)
            #calculate the f value of the neighbor
            neighbor.f = neighbor.g + neighbor.h
            #if the neighbor is not in the open list, add it to the open list
            if neighbor not in open_list:
                open_list.append(neighbor)