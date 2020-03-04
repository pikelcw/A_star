import numpy as np
import pandas as pd
import sys
import time
import argparse
from util import *
from Node import Node
from NodeList import NodeList


@timmer
def astar(maze, start, end, keepDistance):
    h, w = maze.shape
    disMap = mazeToDistanceGrid(maze)

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

            # Keep path away from wall. Add cost according to how far away it is from wall.
            if keepDistance:
                child.updateDisCost(disMap[child_position[0],child_position[1]])
            
            # If child in open list and orignal g is smaller, explore next nighbor
            if open_list.checkInList(child):
                continue
            
            # Add child to open list
            open_list.append(child)
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('map',nargs='?',default='map1.csv',help='Map\'s Name')
    parser.add_argument('--keepDistance','-kd',action='store_true',help='Keep distance from walls')
    args = parser.parse_args()
    print(args)
    # try:
        # file_name = sys.argv[1]
    # except:
        # file_name = "map1.csv"
        # print('No maze specified, use default sample maze.')
    file_name = args.map
    maze, start_pos, end_pos= readInMaze(file_name)
    start = Node(start_pos)
    end = Node(end_pos)
    path = astar(maze,start,end,args.keepDistance)

    if path is None:
        # If return path is None, no path find.
        print("Can not find a path!")
    else:
        # Else, find a path, update maze and show.
        updateMaze(maze,path)
        # printMaze(maze)
        plotMaze(maze)
