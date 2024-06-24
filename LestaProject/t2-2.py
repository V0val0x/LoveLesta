from collections import deque

class CircularBufferDeque: #based on collections.deque
    def __init__(self, size):
        self.size = size
        self.buffer = deque(maxlen=size)

    def enqueue(self, item):
        if len(self.buffer) == self.size:
            self.buffer.popleft()
        self.buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty buffer")
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def __str__(self):
        return f"CircularBufferDeque: {list(self.buffer)}"


"""
Обе реализации полностью функционируют и покрывают основные операции добавления и удаления элементов из буфера.

Код структурирован и сопровождается комментариями, поясняющими ключевые моменты реализации.

Реализация на основе deque вероятно будет быстрее для операций добавления и удаления, так как deque оптимизирован для этих операций.

Реализация на основе списка может быть медленнее из-за необходимости управления индексами вручную, особенно при переполнении буфера.
"""