from Tree import buildTree, Node

def traverse(tree, action, search="depth"):
    """ An iterative traversal of either breadth-first or depth-first search """
    stack = [tree]
    while(stack):
        node = stack.pop(0)
        if action(node) == 1:
            break
        stack = node.getChildren() + stack if search == "depth" else stack + node.getChildren()

if __name__ == "__main__":

    # Build the given Tree
    garmin = buildTree([
        (2, "start"),
        (1, "A1"),
        (2, "A2"),
        (1, "D1"),
        (1, "B1"),
        (1, "B2"),
        (0, "E1"),
        (0, "FindMe"),
        (0, "C1")
    ])

    # The traversal action
    def findme(node):
        print(node.getName())
        if node.getName() == "FindMe":
            return 1
        return 0

    traverse(garmin, findme)
