# CS560 Algorithms Group Project: Finding the Minimal-Cost Path of Hex Grid   
#
# Created by: 
# Alexander Pearson-Goulart, Daniel Hernandez, Neha Nene, 
# Gautham Dixit, and Nick Girard
#
# This program will find the minimal-cost path of a rectangular hex grid using
# the A* algorithm


# Check if node is a right wall
def isRightWall(index):
    return (0 == (index - 8) % 15)

# Check if node is a left wall
def isLeftWall(index):
    return (0 == (index - 1) % 15)

# Get the neighbors that are surrounding a node
def getNeighbors(idx):
    neighbors = {}  # holds values of neighbors
    pathDir = []  # holds direction to each neighbor

    index = int(idx)
    goUp = index - 15
    goTopRight = index - 7
    goDownRight = index + 8
    goDown = index + 15
    goDownLeft = index + 7
    goTopLeft = index - 8

    if goUp > 0 and grid[str(goUp)] != -1:  # go up
        neighbors[str(goUp)] = grid[str(goUp)]
        pathDir.append(1)

    if goTopRight > 0 and not isRightWall(index) and grid[str(goTopRight)] != -1:  # go top right
        neighbors[str(goTopRight)] = grid[str(goTopRight)]
        pathDir.append(2)

    if goDownRight < 233 and not isRightWall(index) and grid[str(goDownRight)] != -1:  # go bottom right
        neighbors[str(goDownRight)] = grid[str(goDownRight)]
        pathDir.append(3)

    if goDown < 233 and grid[str(goDown)] != -1:  # go bottom
        neighbors[str(goDown)] = grid[str(goDown)]
        pathDir.append(4)

    if goDownLeft < 233 and not isLeftWall(index) and grid[str(goDownLeft)] != -1:  # go down left
        neighbors[str(goDownLeft)] = grid[str(goDownLeft)]
        pathDir.append(5)

    if goTopLeft > 0 and not isLeftWall(index) and grid[str(goTopLeft)] != -1:  # go top left
        neighbors[str(goTopLeft)] = grid[str(goTopLeft)]
        pathDir.append(6)

    return neighbors, pathDir


start = '226'  # Start key
end = '8'  # End key
grid = {}  # Hex grid

shortest_distance = {}  # Saves shortest cost path to each hex panel
predecessor = {}  # Keeps track of path
unseenPanels = {}  # Copy of traversable panels
path = []
infinity = 9999999  # Used to indicate panel not traversed thru

''' Places all the values in the text file in a dictionary '''
with open("input.txt") as file:
    for lines in file:
        if not lines.strip():
            continue
        else:
            idx, val = lines.partition(" ")[::2]
            grid[idx] = int(val)
file.close()

''' Copy traversable panels '''
for key, value in grid.items():
    if grid[key] != -1:
        unseenPanels[key] = value

''' Store infinity to all traversable panels to indicate not seen'''
for node in unseenPanels:
    shortest_distance[node] = infinity

shortest_distance[start] = grid[start]  # Initialize starting panel 226

while unseenPanels:
    minNode = None

    ''' Store minimum panel at current time '''
    for node in unseenPanels:
        if minNode is None:
            minNode = node
        elif shortest_distance[node] < shortest_distance[minNode]:
            minNode = node

    n, p = getNeighbors(minNode)  # Get panels able to go thru

    ''' If panel hasn't been visited, find lowest cost and store in shortest_distance '''
    for childNode, val in n.items():
        if childNode != minNode:
            if val + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = val + shortest_distance[minNode]
                predecessor[childNode] = minNode  # Store panel it came from for backtrack
    unseenPanels.pop(minNode)  # Pop unseen to indicate has been seen

# Get the minimal cost from shortest path
finalCost = shortest_distance['8']

# Create path array for shortest path
final = end
while final != start:
    path.insert(0, final)
    final = predecessor[final]

path.insert(0,start)

# print out the final path and total minimal cost of the path and output it to the Output.txt file
finalPath = list(map(str, path))
f = open("Output.txt", "w")
for node in finalPath:
    f.write(str(node) + "\n")
f.write("Minimal-Cost Path Costs: " + str(finalCost))
print("\n".join(finalPath))
print("Minimal-Cost Path Costs: %d" % finalCost)
f.close()