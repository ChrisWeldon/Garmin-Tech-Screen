# Garmin Technical Screen
Chris W. Evans, November 2020

To download and install:
```
git clone https://github.com/ChrisWeldon/Garmin-Tech-Screen
```
To run:
```
python traverse.py
```

## Documentation:

To build an m-ary tree, use `Tree.buildTree(tree)` with the tree parameter of tree being the form:
```
[
    (<number of children>, <name-of-node>),
    ...
]
```

eg.

The tree

can be constructed like so:
```
buildTree([
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
```
To traverse the tree use function `traverse.traverse(tree, action)` with kwarg `search='breadth'` or `search='depth'`.
The traversal defaults to *Depth-First* because it will finish in less steps than *Breadth-First*. Although can be switched with the `search` parameter.

`tree` is a reference to the root of the tree to be traversed.
`action` is a function pointer with 1 param of type `<Tree.Node>` which describes how to behave on each node of traversal.

if `action` returns 1, traversal is halted.

eg.
```
def findme(node):
    print(node.getName())
    if node.getName() == "FindMe":
        return 1
    return 0
```
