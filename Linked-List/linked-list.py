# Singly Linked List
class SingleyList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    

Head = SingleyList(1)
A = SingleyList(3)
B = SingleyList(5)
C = SingleyList(7)

Head.next = A
A.next = B
B.next = C

#Displaying the Linked List
def displayList(head):
    current = Head
    linked_list = []
    while current:
        linked_list.append(str(current.val))
        current = current.next
    print(' -> '.join(linked_list))

#Calling the display function
print(displayList(Head))

#Searching for a value in Linked List
def searchVal(head, key):
    current = head
    while current:
        if current.val == key:
            return True
        current = current.next

    return False

#Calling the search function
print(searchVal(Head, 3))
print(searchVal(Head, 6))