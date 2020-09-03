class Node:
    def __init__(self, val): self.leftChild, self.rightChild, self.data = None, None, val

def binary_insert(root, node):
    if root is None:
        root = node
    if node.data > root.data:
        if root.rightChild is None:
            root.rightChild = node
        else:
            binary_insert(root.rightChild, node)
    elif node.data < root.data:
        if root.leftChild is None:
            root.leftChild = node
        else:
            binary_insert(root.leftChild, node)

def remove_node(node):
    if root == node:


def leftMost(root):
    if root < root.leftChild:
        root = root.leftChild
        leftMost(root)
    if root < root.leftChild > root.rightChild:
        root = root.rightChild
        leftMost(root)
    if root.rightChild is None:
        return root

def rightLeast(root):
def inOrder_Print(root):
    if not root:
        return
    inOrder_Print(root.leftChild)
    print(root.data)
    inOrder_Print(root.rightChild)

def main():
    r = Node(3)
    binary_insert(r,Node(7))
    binary_insert(r,Node(5))
    binary_insert(r,Node(1))
    inOrder_Print(r)


if __name__ == '__main__':
    main()


