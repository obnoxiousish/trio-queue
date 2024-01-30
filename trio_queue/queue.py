import collections

class Queue:
    def __init__(self):
        """Initialize a new empty queue"""
        self._queue = collections.deque()
        
    def empty(self):
        return not self._queue
        
    async def get(self):
        """Remove and return an item from the queue
        
        If queue is empty, wait until an item is available.
        """
        
        while self.empty():
            return