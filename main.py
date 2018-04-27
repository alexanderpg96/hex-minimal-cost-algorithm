# Put the index numbers into an array

# Put the cost numbers into an array

# get neighbors for index; returns neighbors and actions
def isRightWall(index):
    return (0 == (index - 8) % 15 )

def isLeftWall(index):
    return (0 == (index - 1) % 15 )

def getNeighbors (index):
    neighbors = [] #holds values of neighbors
    pathDir = [] #holds direction to each neighbor

    goUp = index - 15
    goTopRight = index - 7
    goDownRight = index + 8
    goDown = index + 15
    goDownLeft = index + 7
    goTopLeft = index - 8

    if goUp > 15 and hexGrid[goUp] != -1: # go up
        neighbors.append(goUp)
        pathDir.append(1)

    if goTopRight > 15 and not isRightWall and hexGrid[goTopRight] != -1 : # go top right
        neighbors.append(goTopRight)
        pathDir.append(2)

    if goDownRight < 218 and not isRightWall and hexGrid[goDownRight] != -1 : #go bottom right
        neighbors.append(goDownRight)
        pathDir.append(3)

    if goDown < 218 and hexGrid[goDown] != -1: #go bottom
        neighbors.append(goDown)
        pathDir.append(4)

    if goDownLeft < 218 and not isLeftWall and hexGrid[goDownLeft] != -1: #go down left
        neighbors.append(goDownLeft)
        pathDir.append(5)

    if goTopLeft > 15 and not isLeftWall and hexGrid[goTopLeft] != -1: #go top left
        neighbors.append(goTopLeft)
        pathDir.append(6)

    return neighbors, pathDir

# get distance from index to finish (distance to goal); returns a number 1 - 10

# print out the indices of the shortest path

# print out the total minimal cost of the path