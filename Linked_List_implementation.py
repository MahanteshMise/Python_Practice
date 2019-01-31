class LinkedStack:
    class Node:

        name = 'Saurabh'

        __slots__ = 'element', 'next'

        def __init__(self, element, next_e):
            self.element = element
            self.next = next_e





    def __init__(self):
        """Creating an empty list"""
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size += 1

    def top(self):

        if self.is_empty():
            raise Empty('Stack is empty')
        return self.head.element

    def pop(self):

        if self.is_empty():
            raise Empty('Stack is empty')

        answer = self.head.element
        self.head = self.head.next
        self.size -= 1

        return answer

    def display(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        while self.head != None:
            print(self.head.element)
            # print('-------{}------'.format(self.Node(23, None).element))
            # print('-------{}------'.format(self.Node(23, self.head.next).next))
            # print(self.head)
            self.head = self.head.next


x = LinkedStack()
# print('-------{}------'.format(x.Node().element))
# print('-------{}------'.format(x.Node().next))
x.push(3)

x.push(4)
x.push(5)

x.display()
