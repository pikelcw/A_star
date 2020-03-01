import numpy as np
import pandas as pd

def readInMap(file):
    # Read in map file
    maze = np.loadtxt("data/"+file, delimiter=',', dtype = int)
    print(maze)
    return maze

class Node():
    def __init__(self, parrnt=None, position=None):
        self.parent = parent
        self.position = position
        
        self.g = 0 
        self.h = 0 
        self.f = 0 

def astar(maze, start, end):
    # Initialze open and closed list
    open_list = []
    closed_list = []
    
    # Add the start point
    open_list.append(start)

if __name__ == "__main__":
    readInMap("map1.csv")
