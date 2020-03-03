import numpy as np
import pandas as pd
import sys
import time
from util import *
from Node import Node
from NodeList import NodeList

@timmer
def astar(maze, start, end):
    h, w = maze.shape
    # Initialze open and closed list
    open_list = NodeList(sort=True)
    closed_list = NodeList()
    
    # Add the start point to open list
    open_list.append(start)

    while(len(open_list) > 0 ):
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        
        if current_node == end: # Find a path
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] # Return reversed path
        
        # Explore Neighboring Nodes
        for neighboring_pos in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            child_position = [current_node.position[0] + neighboring_pos[0], current_node.position[1] + neighboring_pos[1]]

            # Make sure within range, if not, explore next neighbor
            if child_position[0] > (h - 1) or child_position[0] < 0 or child_position[1] > (w - 1) or child_position[1] < 0:
                continue

            # If is wall, explore next neighbor
            if maze[child_position[0],child_position[1]]== 1:
                continue
            
            # Create new child node
            child = Node(child_position, current_node)
            
            # If in closed list, explore next neighbor
            if closed_list.checkInList(child):
                continue
            
            # Calculate cost
            child.updateCost(end)
            
            # If child in open list and orignal g is smaller, explore next nighbor
            if open_list.checkInList(child):
                continue
           
            open_list.append(child)
        # time.sleep(5)
    return None

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except:
        file_name = "map1.csv"
        print('No maze specified, use default sample maze.')
    maze, start_pos, end_pos= readInMaze(file_name)
    start = Node(start_pos)
    end = Node(end_pos)
    path = astar(maze,start,end)
    if path is None:
        print("Can not find a path!")
        quit()
    updateMaze(maze,path)
    printMaze(maze)
    plotMaze(maze)
