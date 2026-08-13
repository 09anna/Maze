import sys

class Node():
    def __init__(self, state, parent, action):
        self.state=state
        self.parent=parent
        self.action=action

class StackFrontier():
    def __init__(self):
        self.frontier=[] #Empty list

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state): #checking whether a particular state already exits in frontier
        for node in self.frontier:
            if node.state==state:
                return True
        return False
