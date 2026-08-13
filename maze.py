import sys

class Node():
    def __init__(self, state, parent, action):
        self.state=state
        self.parent=parent
        self.action=action

class StackFrontier():
    def __init__(self):
        self.frontier=[] #Empty list

    def add(self, node):  #adding somrthing to a frontier
        self.frontier.append(node)

    def contains_state(self, state): #checking whether a particular state already exits in frontier
        for node in self.frontier:
            if node.state==state:
                return True
        return False

    def empty(self): #check if the frontier is empty
        return len(self.frontier)==0

    def remove(self):  #removing from the frontier
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node= self.frontier[-1] #last item
            self.frontier=self.frontier[:-1] 
            return node

