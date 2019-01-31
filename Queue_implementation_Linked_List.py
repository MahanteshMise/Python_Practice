class Linked_Queue:
    class Node:

        def __init__(self, element, next_1):
            self.element = element
            self.next = next_1

    def __init__(self):
        """Creating two reference variables to map head and tail"""
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size += 1

    def first(self):
        if self.size == 0:
            raise Empty("The Queue is Empty")
        else:
            return self.head

    def enqueue(self, e):
        """Appending an element and designing for the case when there is no element and when there is element"""
        if self.size == 0:
            self.head = self.Node(e, None)
            self.size += 1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = self.Node(e, None)
            self.size += 1

    def dequeue(self):
        """Removing an element from the list"""
        if self.size == 0:
            raise Empty("The Queue is empty")
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            answer = curr.element
            curr.next = None
            return answer

    def display(self):
        if self.is_empty():
            print("The list is empty")
        else:
            curr = self.head
            while curr.next is not None:
                print(curr.element)
                curr = curr.next
            else:
                print(curr.element)

x = Linked_Queue()
x.enqueue(3)
x.display()
x.enqueue(4)
x.enqueue(5)
print(x.dequeue())
x.display()