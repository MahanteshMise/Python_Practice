class LinkedQueue:
    class Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next_1):
            self.element = element
            self.next = next_1

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        if self.is_empty():
            self.head = self.Node(e, None)
            self.tail = self.head
            self.size += 1
        else:
            newest = self.Node(e, None)
            self.tail.next = newest
            self.tail = newest
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            return "The Queue is Empty"
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None

        return answer

    def display(self):
        if self.is_empty():
            print("The list is empty")
        else:
            curr = self.head
            # print(curr)
            # print(type(curr))
            while curr.next is not None:
                print(curr.element)
                curr = curr.next
            else:
                print(curr.element)


x = LinkedQueue()
x.enqueue(3)
x.enqueue(4)
x.enqueue(5)
x.display()
x.dequeue()
x.display()
x.dequeue()
x.display()
x.dequeue()
x.display()




