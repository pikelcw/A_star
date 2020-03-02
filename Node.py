import numpy as np
from numpy.linalg import norm

class Node():
    def __init__(self, position=None, parent=None):
        self.parent = parent
        self.position = np.array(position)
        
        self.g = 0 
        self.h = 0 
        self.f = 0 
    
    def returnCost(self):
        return self.f
    
    def updateCost(self,end):
        self.g = self.parent.g + norm(self.position-self.parent.position)
        self.h = norm(self.position-end.position)
        self.f = self.g + self.h

    def __eq__(self,com):
        return np.array_equal(self.position, com.position)
    def __repr__(self):
        return f"Node at {self.position}, with g={self.g}, h={self.h}, f={self.f}."

