import numpy as np
import pandas as pd
import time

def readInMap(file):
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

class Node():
    def __init__(self, position=None, parent=None):
        self.parent = parent
        self.position = position
        
        self.g = 0 
        self.h = 0 
        self.f = 0 
    
    def returnCost(self):
        return self.f
    
    def updateCost(self,end):
        self.g = self.parent.g + ((self.position[0]-self.parent.position[0])**2+(self.position[1]-self.parent.position[1])**2)**(1/2)
        self.h = (((self.position[0] - end.position[0]) ** 2) + ((self.position[1] - end.position[1]) ** 2))**(1/2)
        self.f = self.g + self.h

    def __eq__(self,com):
        return self.position == com.position

    def __repr__(self):
        return f"Node at {self.position}, with g={self.g}, h={self.h}, f={self.f}."

def astar(maze, start, end):
    h, w = maze.shape
    # Initialze open and closed list
    open_list = []
    closed_list = []
    
    # Add the start point to open list
    open_list.append(start)

    while(len(open_list) > 0 ):
        # print("While")
        open_list.sort(key = Node.returnCost)
        # for closed_node in closed_list:
        #     print(closed_node.position)
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        print(current_node)
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
            for closed in closed_list:
                # print(child,closed)
                if child == closed:
                    # print("child in closed list")
                    break
            else:
                child.updateCost(end)

                for open_node in open_list:
                    if child == open_node and child.g >= open_node.g:
                        # print("Chile in open list")
                        break
                else:
                    print("Add",child)
                    open_list.append(child)
        # time.sleep(5)
    return None

if __name__ == "__main__":
    maze, start_pos, end_pos= readInMap("map2.csv")
    start = Node(start_pos)
    end = Node(end_pos)
    path = astar(maze,start,end)
    print(path)
