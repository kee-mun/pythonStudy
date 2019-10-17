class node:
    def __init__(self, data):
        self.data = data
        self.downNode = None

class stackNode:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        if self.top == None:
            self.top = node(data)
        else:
            self.top.downNode, self.top = self.top, node(data)