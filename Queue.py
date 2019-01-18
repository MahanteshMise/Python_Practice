class Queue(object):

    def __init__(self):

        self.queue_items = []

    def enqueue(self, item):
        self.queue_items.insert(0, item)

    def dequeue(self):
        return self.queue_items.pop()

    def isEmpty(self):
        return self.queue_items == []

    def size(self):
        return len(self.queue_items)

t = Queue()
t.enqueue(4)
t.enqueue(5)
t.enqueue(6)
t.size()
print(t.queue_items)
print(t.dequeue())
print(t.dequeue())
t.isEmpty()
print(t.dequeue())
print(t.queue_items)



