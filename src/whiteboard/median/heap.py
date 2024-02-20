import operator


# A heap object stolen from  Pieter Mulder
# https://github.com/inytar/algorithm-studies/blob/master/trees%202016_12_09.ipynb

class Heap(object):
    """
    A Heap (by default, a min heap)
    """
    
    def __init__(self, key=operator.lt):
        """Create a heap of iterator, defaults to a minHeap (smallest value at root)."""

        self._heap = [None, ]
        self._length = 0
        self.key = key


    def __iter__(self):
        """Return an ordered iterator."""
        for i in range(self._length):
            yield self.pop()


    @property
    def length(self):
        return self._length

    @staticmethod
    def _get_parent_index(index):
        return (index) // 2
    
    @staticmethod
    def _get_right_index(index):
        return (index) * 2 + 1
    
    @staticmethod
    def _get_left_index(index):
        return (index) * 2
    
    def insert(self, item):
        self._heap.append(item)
        self._length += 1
        self._swap_up(self._length)

    def peek(self):
        return self._heap[1]
        
    def pop(self):
        value = self._heap[1]
        try:
            self._heap[1] = self._heap.pop() 
        except IndexError:
            # Special case for popping off the last element.
            # Don't swap down if the heap is empty.
            pass
        else:
            self._swap_down(1)
        self._length -= 1
        return value
    
    def _swap_down(self, index):
        value = self._heap[index]
        left_i = self._get_left_index(index)
        try:
            left = self._heap[left_i]
        except IndexError:
            # Last node in tree we are done.
            return
        right_i = self._get_right_index(index)
        try:
            right = self._heap[right_i]
        except IndexError:
            # Node does not have a right child, only use the left.
            child = left
            child_index = left_i
            # for printing
            right = None
        else:
            if self.key(left, right):
                child = left
                child_index = left_i
            else:
                child = right
                child_index = right_i
        if not self.key(value, child):
            self._heap[child_index] = value
            self._heap[index] = child
            self._swap_down(child_index)

    def _swap_up(self, index):
        value = self._heap[index]
        parent_index = self._get_parent_index(index)
        parent = self._heap[parent_index]
        if parent is not None and self.key(value,parent):
            self._heap[parent_index] = value
            self._heap[index] = parent
            self._swap_up(parent_index)
            
    def __str__(self):
        return self._heap[1:].__str__()
    
    def __repr__(self):
        return self._heap.__str__()


def main():
    h1 = Heap(operator.lt) # min heap.
    h2 = Heap(operator.gt) # max heap.
    for e in range(10):
        h1.insert(e)
        h2.insert(e)

    print(h1.peek())
    print(h2.peek())
    

if __name__ == "__main__":
    main()
