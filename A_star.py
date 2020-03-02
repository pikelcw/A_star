import numpy as np
import pandas as pd
import time
from util import *
from Node import Node
from NodeList import NodeList

def astar(maze, start, end):
    h, w = maze.shape
    # Initialze open and closed list
    open_list = NodeList(sort=True)
    closed_list = NodeList()
    
    # Add the start point to open list
    open_list.append(start)

    while(len(open_list) > 0 ):
        # print("While")
        # open_list.sort(key = Node.returnCost)
        # for closed_node in closed_list:
        #     print(closed_node.position)
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        # print(current_node)
        if current_node == end: # Find a path
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] # Return reversed path
        children = []
        for neighboring_pos in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            child_position = [current_node.position[0] + neighboring_pos[0], current_node.position[1] + neighboring_pos[1]]

            # Make sure within range
            if child_position[0] > (h - 1) or child_position[0] < 0 or child_position[1] > (w - 1) or child_position[1] < 0:
                continue

            # If is wall, conitnue
            if maze[child_position[0],child_position[1]]== 1:
                continue
            
            child_node = Node(child_position, current_node)
            children.append(child_node)

        for child in children:
            if closed_list.checkInList(child):
                continue
            
            child.updateCost(end)
            
            if open_list.checkInList(child):
                continue
           
            # print("Add",child)
            open_list.append(child)
        # time.sleep(5)
    return None

if __name__ == "__main__":
    maze, start_pos, end_pos= readInMaze("map2.csv")
    start = Node(start_pos)
    end = Node(end_pos)
    path = astar(maze,start,end)
    # print(path)
    updateMaze(maze,path)
    printMaze(maze)
    plotMaze(maze)
