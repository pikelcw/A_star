import numpy as np
import matplotlib.pyplot as plt

def readInMaze(file):
    '''
       Read in map file
       0 : open cell
       1 : wall
       2 : start point
       3 : end point
    '''
    maze = np.loadtxt("data/"+file, delimiter=',', dtype = int)
    # print(maze)
    start_pos = None
    end_pos = None
    for i,row in enumerate(maze):
        for j,cell in enumerate(row):
            if cell == 2:
                start_pos = [i,j]
            if cell == 3:
                end_pos = [i,j]

    assert start_pos is not None, "No starting point"
    assert end_pos is not None, "No ending point"

    return maze,start_pos,end_pos
def printMaze(maze):
    print(maze)

def  updateMaze(maze,path):
    for y,x in path[1:-1]:
        maze[y,x] = 9

def plotMaze(maze):
    print(type(maze))
    plt.imshow(maze)
    plt.show()

