class Stack(object):

    def __init__(self):
        self.item_list = []

    def push(self,qnty):
        self.item_list.append(qnty)

    def pop(self):
        return  self.item_list.pop()

    def peek(self):
        return self.item_list[len(self.item_list)-1]

    def size(self):
        return len(self.item_list)

    def isEmpty(self):
        return len(self.item_list) == 0

    def multiple_push(self,*args):
        for item in args:
            self.push(item)



t = Stack()
t.push(3)
t.push(4)
print(t.item_list)
t.multiple_push(5,6,7,8,9,10)
print(t.item_list)