import numpy as np
import matplotlib.pyplot as plt
import time
def readInMaze(file):
    '''
       Read in map file
       0 : open cell
       1 : wall
       2 : start point
       3 : end point
    '''
    maze = np.loadtxt("data/"+file, delimiter=',', dtype = int)
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

def updateMaze(maze,path):
    for y,x in path[1:-1]:
        maze[y,x] = 9

def plotMaze(maze):
    image = np.ones((maze.shape[0],maze.shape[1],3))
    for j,row in enumerate(maze):
        for i,element in enumerate(row):
            if element == 1:
                image[j,i,:] = np.array([0,0,0])
            elif element == 2:
                image[j,i,:] = np.array([1,0,0])
            elif element == 3:
                image[j,i,:] = np.array([0,1,0])
            elif element == 9:
                image[j,i,:] = np.array([0,0,1])

    plt.imshow(image)
    plt.show()

def timmer(method):
    def time_it(*args,**kargs):
        start = time.time()
        result = method(*args,**kargs)
        dur = time.time()-start
        print(f"It used {dur} sec.")
        return result
    return time_it

