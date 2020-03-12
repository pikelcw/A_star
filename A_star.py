import numpy as np
import pandas as pd
import sys
import time
import argparse
from util import *
from Node import Node
from NodeList import NodeList


def astar(maze, start, end, keepDistance, verbose):
    h, w = maze.shape
    totalPix = np.sum(maze!=1)
    if keepDistance:
        disMap = mazeToDistanceGrid(maze)
    if verbose:
        maze_cp = maze.copy()
        plotMaze(maze_cp)
    # Initialze open and closed list
    open_list = NodeList(sort=True)
    closed_list = NodeList()
    
    # Add the start point to open list
    open_list.append(start)

    while(len(open_list) > 0 ):
        if verbose:
            plotMaze(maze_cp)
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        if verbose and current_node != start:
            maze_cp[current_node.position[0],current_node.position[1]] = 4
        
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
            if verbose:
                maze_cp[child.position[0],child.position[1]] = 5

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('map',nargs='?',default='map1.csv',help='Map\'s Name')
    parser.add_argument('--keepDistance','-kd',action='store_true',help='Keep distance from walls')
    parser.add_argument('--verbose','-v',action='store_true',help='Verbose solving status')
    args = parser.parse_args()
    file_name = args.map
    maze, start_pos, end_pos= readInMaze(file_name)
    start = Node(start_pos)
    end = Node(end_pos)
    path = astar(maze,start,end,args.keepDistance,args.verbose)

    if path is None:
        print("Can not find a path!")
        plotMaze(maze,hold = True)
    else:
        # Else, find a path, update maze and show.
        maze = updateMaze(maze,path)
        # printMaze(maze)
        plotMaze(maze,hold = True)
