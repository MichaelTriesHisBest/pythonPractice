class Node:
    def __init__(self, val): self.next, self.previous, self.data = None, None, val


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def Emptyness(self):
        if self.count == 0:
            return True
        else:
            return False

    def addToBeginning(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = self.head
            self.count += 1
        else:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
            self.count += 1

    def addToEnd(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.previous = self.tail
            self.tail = newNode
            self.count += 1

    def remove(self, node):

        if self.count == 1:
            self.head = None
        if self.head == node:
            self.head = node.next
        if node.previous is not None:
            node.previous.next = node.next
        if node.next is not None:
            node.next.previous = node.previous
        if node == self.tail:
            self.tail = node.previous
        self.count -= 1

    def removeAt(self, index):

        newNode = self.head
        for i in range(0, self.count) and newNode.next is not None:
            if i > self.count:
                print('The index is out of bounds')
            elif i == index:
                remove(newNode)
            else:
                newNode = newNode.next

    def removeFromTail(self):

        if self.tail is not None:
            print("The tail you've removed is :", self.tail.data)
            self.tail = self.tail.previous
            removeAt(self.count - 1)

    def removeSpecifiedNode(self, data):
        newNode = self.head
        for i in range(0, self.count):
            if newNode.data == data:
                removeAt(i)
            else:
                newNode = newNode.next

    def printDoublyLinkedList(self):
        newNode = self.head
        for i in range(0, self.count):
            print(newNode.data)
            newNode = newNode.next


def main():
    linkedList = DoublyLinkedList()
    linkedList.addToBeginning('5')
    linkedList.Emptyness()
    linkedList.addToBeginning('55')
    linkedList.addToEnd('Tuesday')
    linkedList.addToEnd('Wednesday')
    linkedList.addToBeginning('Friday')
    linkedList.removeFromTail()
    linkedList.printDoublyLinkedList()


if __name__ == '__main__':
    main()
