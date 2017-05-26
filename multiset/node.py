"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.
"""

class Node(object):

    def __init__(self, data, counts = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = counts

class TwoWayNode(Node):

    def __init__(self, data, previous=None, counts = None):
        Node.__init__(self, data, counts)
        self.previous = previous

# Just an empty link
node1 = None

# A node containing data and an empty link
node2 = Node("A", None)

# A node containing data and a link to node2
node3 = Node("B", node2)
