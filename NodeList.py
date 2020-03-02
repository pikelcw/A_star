from Node import Node
class NodeList():
    def __init__(self,sort=False):
        self.node_list = []
        self.sort = sort
    def append(self,node):
        self.node_list.append(node)
        if self.sort:
            self.node_list.sort(key = Node.returnCost)
    def pop(self,idx):
        return self.node_list.pop(idx)
    def __len__(self):
        return len(self.node_list)
    def checkInList(self,node):
        for element in self.node_list:
            # print(child,closed)
            if node == element:
                # print("child in closed list")
                return True
        return False

