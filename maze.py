import sys

class Node():
    def __init__(self, state, parent, action):
        self.state=state
        self.parent=parent
        self.action=action

class StackFrontier():
    def __init__(self):
        self.frontier=[] #list

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        