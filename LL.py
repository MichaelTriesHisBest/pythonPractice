class Node:
    def __init__(self, val): self.next, self.data = None, val


class LinkedlinkedList:
    def __init__(self):
        self.head = None

    def addToBeginning(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head.next
            self.head = newNode

    def addToEnd(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def searchList(self, data):
        temp_Node = self.head
        while temp_Node.next is not None:
            if temp_Node.data == data:
                print("Found!")
                return temp_Node
            else:
                temp_Node = temp_Node.next

    def printlinkedList(self):
        printedValue = self.head
        while printedValue is not None:
            print(printedValue.data)
            printedValue = printedValue.next

    def insert_after_X(self, NewData, OldData):
        temp = self.head
        while temp is not None:
            if temp.data == OldData:
                break
            temp = temp.next
        if temp is None:
            print("Oops!")
        else:
            new_node = Node(NewData)
            new_node.next = temp.next
            temp.next = new_node

    def insert_before_item(self, x, data):
        newNode = Node(data)
        temp_Node = self.head
        if self.head is None:
            print("REEEE")
            return
        if x == self.head.data:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            # You assign the head to the node after newNode, and then assign newNode as the new head.
            return
        while temp_Node.next is not None:
            if temp_Node.next.data == x:
                break
            temp_Node = temp_Node.next
        if temp_Node is None:
            print("Item is not in the linkedList!")
        else:
            newNode.next = temp_Node.next
            temp_Node.next = newNode

    def insert_at_Loc(self, index, data):
        newNode = Node(data)
        temp_Node = self.head
        i = 0
        while i <= index and temp_Node.next is not None:
            if i == index:
                newNode.next = self.head
                self.head = newNode
                break
            else:
                temp_Node = temp_Node.next
                i += 1

    def amount_in_Lists(self):
        temp_Node = self.head
        i = 0
        while temp_Node.next is not None:
            temp_Node = temp_Node.next
            i += 1
        print("The number of nodes in this list are: ", i)


def main():
    linkedList = LinkedlinkedList()
    linkedList.addToBeginning("Big")
    linkedList.addToEnd("Mon")
    linkedList.addToEnd("Tuesday")
    linkedList.addToEnd("Thursday")
    linkedList.addToBeginning("Beginning")
    linkedList.insert_after_X("Monday", 'Mon')
    linkedList.insert_before_item("Tuesday", "Tue")
    linkedList.insert_at_Loc(3, 'Tittiy')
    linkedList.amount_in_Lists()
    linkedList.searchList('Monday')
    linkedList.printlinkedList()


if __name__ == '__main__':
    main()
