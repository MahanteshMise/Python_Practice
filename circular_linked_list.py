class CircularLinkedList:

    class Node:

        def __init__(self, element, next_1):
            self.element = element
            self.next = next_1


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0


    def enqueue(self,e):
        newest = self.Node(e, None)

        if self.is_empty():
            self.head = newest
            self.tail = newest
            newest.next = newest
            self.size += 1
        else:
            newest.next = self.tail.next
            self.tail.next = newest
            self.tail = self.tail.next
            self.size += 1

    def dequeue(self):

        if self.is_empty():
            return "The circular linked list is empty"
        elif(self.size == 1):
            answer = self.head.element
            self.head = None
            self.tail = None
            self.size -= 1
            return answer
        else:
            answer = self.head.element
            self.tail.next = self.head.next
            self.head = self.head.next
            self.size -= 1
            return answer


    def display(self):
        if self.is_empty():
            return "The circular linked list is empty"
        elif self.size == 1:
            return self.head.element
        else:
            print(self.head.element)
            comp = self.head.next
            while self.head != comp.next:
                print(comp.element)
                comp = comp.next
            print(comp.element)

x = CircularLinkedList()
x.enqueue(3)
x.enqueue(4)
x.enqueue(5)
x.display()
print(x.dequeue())
print(('----------------------------------'))
x.display()
print(('----------------------------------'))
print(x.dequeue())
print(('----------------------------------'))
x.display()
print(('----------------------------------'))
print(x.dequeue())
print(('----------------------------------'))
x.display()
print(x.dequeue())