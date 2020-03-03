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
        if self.sort: 
            check = self.checkSort
        else:
            check = self.checkUnsort

        for element in self.node_list:
            if check(node,element):
                return True
        return False

    def checkSort(self,node,element):
        return ((node == element) and (node.g >= element.g))

    def checkUnsort(self,node,element):
        return (node == element)
