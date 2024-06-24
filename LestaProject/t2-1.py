class CircularBufferList: #based on regular list
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start = 0
        self.end = 0
        self.is_full = False

    def enqueue(self, item):
        self.buffer[self.end] = item
        if self.is_full:
            self.start = (self.start + 1) % self.size
        self.end = (self.end + 1) % self.size
        self.is_full = self.end == self.start

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty buffer")
        item = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.size
        self.is_full = False
        return item

    def is_empty(self):
        return self.start == self.end and not self.is_full

    def __str__(self):
        if self.is_empty():
            return "CircularBufferList: []"
        items = []
        i = self.start
        while True:
            items.append(self.buffer[i])
            if i == self.end and not self.is_full:
                break
            i = (i + 1) % self.size
        return f"CircularBufferList: {items}"
