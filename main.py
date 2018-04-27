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
def dist_to_goal(index):
    dist22 = 226
    dist21 = [211,219,227]
    dist20 = [196,204,212,220,228]
    dist19 = [181,189,197,205,213,221,229]
    dist18 = [166,174,182,190,198,206,214,222,230]
    dist17 = [151,159,167,175,183,191,199,207,215,223,231]
    dist16 = [136,144,152,160,168,176,184,192,200,208,216,224,232]
    dist15 = [121,129,137,145,153,161,169,177,185,193,201,209,217,225,233]
    dist14 = [1,16,31,46,61,76,91,106,114,122,130,138,146,154,162,170,178,186,194,202,210,218]
    dist13 = [9,24,39,54,69,84,99,107,115,123,131,139,147,155,163,171,179,187,195,203]
    dist12 = [2,17,32,47,62,77,92,100,108,116,124,132,140,148,156,164,172,180,188]
    dist11 = [10,25,40,55,70,85,93,101,109,117,125,133,141,149,157,165,173]
    dist10 = [3,18,33,48,63,78,86,94,102,110,118,126,134,142,150,158]
    dist9 = [11,26,41,56,71,79,87,95,103,111,119,127,135,143]
    dist8 = [4,19,34,49,64,72,80,88,96,104,112,120,128]
    dist7 = [12,27,42,57,65,73,81,89,97,105,113]
    dist6 = [5,20,35,50,58,66,74,82,90,98]
    dist5 = [13,28,43,51,59,67,75,83]
    dist4 = [6,21,36,44,52,60,68]
    dist3 = [14,29,37,45,53]
    dist2 = [7,22,30,38]
    dist1 = [15,23]
    dist0 = 8

    if index == dist22:
        return 22
    elif index in dist21:
        return 21
    elif index in dist20:
        return 20
    elif index in dist19:
        return 19
    elif index in dist18:
        return 18
    elif index in dist17:
        return 17
    elif index in dist16:
        return 16
    elif index in dist15:
        return 15
    elif index in dist14:
        return 14
    elif index in dist13:
        return 13
    elif index in dist12:
        return 12
    elif index in dist11:
        return 11
    elif index in dist10:
        return 10
    elif index in dist9:
        return 9
    elif index in dist8:
        return 8
    elif index in dist7:
        return 7
    elif index in dist6:
        return 6
    elif index in dist5:
        return 5
    elif index in dist4:
        return 4
    elif index in dist3:
        return 3
    elif index in dist2:
        return 2
    elif index in dist1:
        return 1
    elif index  == dist0:
        return 0

# print out the indices of the shortest path

# print out the total minimal cost of the path
finalPath = list(map(str, finalPath))
sys.stdout = open("C:\\Output.txt", "w")
print("\n".join(finalPath))
print("Minimal-Cost Path Costs: %d" % finalCost)
sys.stdout.close()