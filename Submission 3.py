# create the node class for the binary tree
class Node:
    def __init__(self, data):
        self.root = data    # root
        self.left = ""    # left child
        self.right = ""   # right child


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(self.root, data)

    def _add(self, data, node):
        if data < node.root:
            print('Going Left!')
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            print('Going Right!')
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data is node.root:
            return node
        elif data < node.root and node.left is not None:
            self._find(data, node.left)
        elif data > node.root and node.right is not None:
            self._find(data, node.right)

    def delTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.root) + '  ')
            self._printTree(node.right)


moreGuests = ()
tree = Tree()
#tree.add('M')
moreGuests = input("Do you need to start a guest list?")
exitGuestList = ()
while exitGuestList is not 'no':
    if moreGuests == 'yes':
        # guestName =
        tree.add(input("Enter the guest name Last Name first with no punctuation:"))
        moreGuests = input("Do you need to add another guest? ('yes' or 'no' only)")
    if moreGuests == 'no':
        doprint = input("Are you ready to print now? ('yes' or 'no' only)")
        if doprint == 'yes':
            print("=" * 25)
            print("Wedding Seating")
            print("=" * 25)
            tree.printTree()
        if doprint == 'no':
            exitGuestList = input("Do you need to exit?")
        if exitGuestList is 'no':
            exit()
    if moreGuests is not 'yes' and moreGuests is not 'no':
        moreGuests = input("Input error. Use 'yes' or 'no' only.")
