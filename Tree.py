""" A module containing classes and helper functions for the m-ary tree. """

class Node:
    """ A definition for tree node.
    This node is defined in the given document for the Garmin technical screen challenge.
    """
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __repr__(self):
        return "<" + self.name + " - "+ str(len(self.children)) +">"

    def setChildren(self, children):
        self.children = children

    def getChildren(self):
        return self.children

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

def buildTree(tree_list):
    """
    A helper function for building trees from an array of tuples.
    [ (<number-of-children>, <name-of-node>), ... ]

    eg.
    [(2, start), (3, A1), (1, A2), (1, B1), (0, B2), (0, B3), (1, B4), (0, C1), (0, C2)]

         "Start"
         ___|___
        "A1"   "A2"
     ____|___    |
     |   |  |    \
    "B1" "B2""B3"  "B4"
     |               |
    "C1"            "C2"
    """

    parse_queue = tree_list.copy()
    root = Node(parse_queue[0][1], [None for i in range(parse_queue[0][0])])
    parse_queue = parse_queue[1:]

    child_queue = [root]
    while(child_queue):
        # Build tree iteratively
        node = child_queue.pop(0)
        for c in range(len(node.getChildren())):
            parse = parse_queue.pop(0)
            # Populate tree with empty nodes, then come back on next iteration
            child = Node(parse[1], [None for i in range(parse[0])])
            node.getChildren()[c] = child
            child_queue.append(child)

    return root
