class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def pop(self):
        self.size = self.size - 1
        self.stack.pop()

    def push(self, n):
        self.size += 1
        self.stack.append(n)

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def sizeOf(self):
        return self.size

    def maxValue(self):
        maxVal = self.stack[0]
        for x in self.stack:
            if self.stack[x] > maxVal:
                maxVal = self.stack[x]
        return maxVal

    def leastVal(self):
        leastVal = self.stack[0]
        for x in self.stack:
            if self.stack[x] < leastVal:
                leastVal = self.stack[x]
        return leastVal

    def sortStack(self):
        for i in range(1, self.size):
            ind = self.stack[i]
            j = i - 1
            while j >= 0 and ind < self.stack[j]:
                self.stack[j + 1] = self.stack[j]
                j -= 1
            self.stack[j + 1] = ind

    def printStack(self):
        n = self.size
        for x in range(n):
            print("[{}] = {}".format({x}, {self.stack[x]}))


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkefinal_node:
    def __init__(self):
        self.size = 0
        self.start_nodeval = None

    # Print the linked list
    def listprint(self):
        printval = self.start_nodeval
        i = 0
        while printval is not None:
            print("Node value {} at Location {}".format(printval.dataval, i))
            printval = printval.nextval
            i += 1

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        self.size += 1
        NewNode.nextval = self.start_nodeval
        self.start_nodeval = NewNode

    def atEnd(self, newdata):
        # NewNode = Node(newdata)
        if self.size == 0:
            SLinkefinal_node.AtBegining(self, newdata)
        lastval = self.start_nodeval
        while lastval.nextval:
            lastval = lastval.nextval
        NewNode = Node(newdata)
        lastval.nextval = NewNode
        self.size += 1

    def atIndex(self, nodedata, index):
        i = 1
        idata = self.start_nodeval
        if index == 0:
            SLinkefinal_node.AtBegining(self, nodedata)
        if index == self.size:
            SLinkefinal_node.atEnd(self, nodedata)
        while idata.nextval:
            if i == index:
                NewNode = Node(nodedata)
                NewNode.nextval = idata.nextval
                idata.nextval = NewNode
            idata = idata.nextval
            i += 1

    def getvalue(self, nodevalue):
        current = self.start_nodeval
        if current.dataval == nodevalue:
            print("Found {}".format(current.dataval))
            return current.dataval
        while current.nextval:
            if current.dataval == nodevalue.dataval:
                # current.dataval = current.nextval
                print("Found!! {}".format(current.dataval))
                return current

            else:
                current = current.nextval
        print("{} not found".format(nodevalue))

    def delete_element_by_value(self, x):
        if self.start_nodeval is None:
            print("The list has no element to delete")
            return

        if self.start_nodeval.dataval == x:
            self.start_nodeval = self.start_nodeval.nextval
            return

        n = self.start_nodeval
        while n.nextval is not None:
            if n.nextval.dataval == x.dataval:
                break
            n = n.nextval

        if n.nextval is None:
            print("item not found in the list")
        else:
            n.nextval = n.nextval.nextval

    def delete_by_index(self, x):
        i = 0
        current = self.start_nodeval
        while i < self.size and current.nextval:
            if i == x:
                value = SLinkefinal_node.getvalue(self, current)
                SLinkefinal_node.delete_element_by_value(self, value)
                return
            current = current.nextval
            i += 1


class DNode:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.prev = None


class DLinkefinal_node:
    def __init__(self):
        self.size = 0
        self.start_node = None
        self.final_node = None

    def getSize(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def addfirst(self, data):
        node = DNode(data)
        if DLinkefinal_node.isEmpty(self):
            self.start_node = node
            self.final_node = node
            self.size += 1
        elif self.size == 1:
            # temp = self.start_node
            node.next = self.start_node
            self.final_node = self.start_node
            self.start_node.prev = node
            self.size += 1
            self.start_node = node
        else:
            node.next = self.start_node
            self.start_node.prev = node
            self.start_node = node
            self.size += 1

    def addlast(self, data):
        if DLinkefinal_node.isEmpty(self):
            DLinkefinal_node.addfirst(self, data)
        elif self.size == 1:
            node = DNode(data)
            node.prev = self.final_node
            self.final_node.next = node
            self.final_node = node
            self.size += 1
        else:
            node = DNode(data)
            node.prev = self.final_node
            self.final_node.next = node
            self.final_node = node
            self.size += 1

    def getIndex(self, data):
        i = 0

        current = self.start_node
        while i < self.size:
            if current.data == data:
                print("The index of value {} is : {}".format(current.data, i))
                return current
            i += 1
            current = current.next

    def removeHead(self):
        if DLinkefinal_node.isEmpty(self):
            return "Empty!"
        if self.size == 1:
            DLinkefinal_node.remove(self, self.start_node)
        else:
            print("Removing {}".format(self.start_node.data))
            self.start_node = self.start_node.next
            self.start_node.prev = None
            self.size -= 1

    def removeByIndex(self, index):
        if index > self.size:
            return "Index Out of Bounds"
        if self.size == 0:
            return "Empty!"
        if index == 0:
            DLinkefinal_node.removeHead(self)
            return
        elif index == self.size:
            DLinkefinal_node.removeTail(self)
            return
        else:
            DLinkefinal_node.remove(self, DLinkefinal_node.getValue(self, index))

    def remove(self, node):
        # checks if the node is the last node
        if self.size == 1:
            print("Removing {}".format(self.start_node.data))
            self.start_node = None
            self.final_node = None
            self.size -= 1
            return
        elif node.next is None:
            print("Removing {}".format(self.final_node.data))
            self.final_node = self.final_node.prev
            self.final_node.next = None
            self.size -= 1
            return
        elif node.prev is None and node.next is not None:
            # checks if the node is the headnode
            print("Removing {}".format(self.start_node.data))
            self.start_node = self.start_node.next
            self.start_node.prev = None
            self.size -= 1

        elif node.next is not None and node.prev is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
            node = None
            self.size -= 1


            return

    def removeTail(self):
        if DLinkefinal_node.isEmpty(self):
            return "Empty!"
        elif self.size == 1:
            DLinkefinal_node.remove(self, self.final_node)
        else:
            DLinkefinal_node.remove(self, self.final_node)

    def getValue(self, index):
        if index > self.size:
            return "Oopsie!"
        i = 0
        current = self.start_node
        while i <= index:
            if i == index:
                print("The VALUE at INDEX {} is : {}".format(index, current.data))
                return current
            current = current.next
            i += 1

    def printForward(self):
        if DLinkefinal_node.isEmpty(self):
            return "Empty!"
        current = self.start_node
        i = 0
        while current is not None:
            print("Index : {} ; Value : {}".format(i, current.data))
            if current.next:
                current = current.next
                i += 1
            else:
                return

    def printBackward(self):
        if DLinkefinal_node.isEmpty(self):
            return "Empty"
        current = self.final_node
        i = self.size - 1
        while current is not None:
            print("Index : {} ; Value : {}".format(i, current.data))
            if current.prev:
                current = current.prev
                i -= 1
            else:
                return


if __name__ == '__main__':
    dddddlist = DLinkedddddlist()
    # dddddlist.start_node = DNode("1")
    i = 0
    while i < 6:
        dddddlist.addfirst(i)
        i += 1

    dddddlist.removeByIndex(3)
    print(dddddlist.size)
    # dddddlist.removeTail()
    dddddlist.printForward()
    # obj = Stack()
    # obj.push(3)
    # obj.push(4)
    # obj.push(1)
    # obj.sortStack()
    # obj.printStack()
    # print(obj.size)

    # list = SLinkedddddlist()
    # # list.start_nodeval = Node("Node 2")
    # # e2 = Node("Node 3")
    # e3 = Node("Node 1")
    # list.AtBegining(e3.dataval)
    # list.atEnd("Node 2")
    # list.atEnd("Node 3")
    # list.atEnd("Node 4")
    # list.atEnd("Node 5")
    # list.atEnd("Node 7")
    # e4 = Node("Node 6")
    # list.atIndex(e4.dataval, 1)
    #
    # print("List Size " + str(list.size))
    # # list.delete_element_by_value("Node 3")
    # list.delete_by_index(1)
    #
    # list.listprint()

# 1 6 2 3 4 5 7
