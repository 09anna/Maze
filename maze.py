import sys

class Node():
    def __init__(self, state, parent, action):
        self.state=state
        self.parent=parent
        self.action=action

class StackFrontier():
    def __init__(self):
        self.frontier=[] #Empty list

    def add(self, node):  #adding something to a frontier
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
            node= self.frontier[-1] #last item (end of the list)
            self.frontier=self.frontier[:-1] #remove the last item
            return node


class QueueFrontier(StackFrontier): #inheriting from StackFrontier
    def remove(self):
        if self.empty():
            raise Exception ("Empty frontier")
        else: node=self.frontier[0] #first node
        self.frontier=self.frontier[1:] #remove beginning of the list
        return node


class Maze(): #handle the process of taking a swquence a maze like text
    def __init__(self, filename):
        #Read file and set height and width of maze
        with open(filename) as f:
            contents=f.read()
        #validate start and goal
        if contents.count("A")!=1: #A representing starting position
            raise Exception("Maze must have exactly one start point")
        if contents.count("B") !=1: #B representing as ending position
            raise Exception("maze must have exactly one goal")


    
