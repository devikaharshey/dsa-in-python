# Doubly Linked List
class doubleyLinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
    
Head = doubleyLinkedList(1)
A = doubleyLinkedList(3)
B = doubleyLinkedList(5)
C = doubleyLinkedList(7)

Head.next = A
A.next = B
B.next = C
C.prev = B
B.prev = A
A.prev = Head

#Displaying the Linked List
def displayListForward(head):
    current = Head
    linked_list = []
    while current:
        linked_list.append(str(current.val))
        current = current.next
    print(' <-> '.join(linked_list))

def displayListBackward(head):
    current = C
    linked_list = []
    while current:
        linked_list.append(str(current.val))
        current = current.prev
    print(' <-> '.join(linked_list))

#Calling the display functions
displayListForward(Head)
displayListBackward(C)

#Inserting a node
def insert_at_beginning(head, tail, val):
    new_node = doubleyLinkedList(val, next=head)
    head.prev = new_node
    return new_node, tail

def insert_at_end(head, tail, val):
    new_node = doubleyLinkedList(val, prev=tail)
    tail.next = new_node
    return head, new_node

#Calling the insert functions
Head, C = insert_at_beginning(Head, C, 0)
Head, C = insert_at_end(Head, C, 9)
displayListForward(Head)