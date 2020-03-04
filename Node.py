import numpy as np
from numpy.linalg import norm

class Node():
    def __init__(self, position=None, parent=None):
        '''
            parent  : parent node
            position: index of maze
            g       : moving cost, distance from starting node to this node
            h       : heuristic cost, linear distance from ending node to this node
            f       : total cost, g+h
        '''
        self.parent = parent
        self.position = np.array(position)
        
        self.g = 0 
        self.h = 0 
        self.f = 0 
    
    def returnCost(self):
        '''
            Return current total cost. For sorting the open list.
        '''
        return self.f
    
    def updateCost(self,end):
        # g = parent's g plus distance from parent
        self.g = self.parent.g + norm(self.position-self.parent.position)
        # h = linear distance from end position to current position
        self.h = norm(self.position-end.position)
        # f = g + h
        self.f = self.g + self.h

    def updateDisCost(self,dis):
        self.f += self.f/dis

    def __eq__(self,com):
        return np.array_equal(self.position, com.position)

    def __repr__(self):
        return f"Node at {self.position}, with g={self.g}, h={self.h}, f={self.f}."

