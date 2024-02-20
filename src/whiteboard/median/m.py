from heap import Heap

import operator

class Median(object):

    def __init__(self):
        self.h1 = Heap(operator.lt) # min heap (for large numbers)
        self.h2 = Heap(operator.gt) # max heap (for small numbers)

    def peek(self):

        if self.h1.length == self.h2.length == 0:
            return None

        if self.h1.length > self.h2.length:
            return self.h1.peek()
        elif self.h2.length > self.h1.length:
            return self.h2.peek()
        else:
            return (self.h1.peek() + self.h2.peek()) / 2

    def insert(self, new):
        # If the heaps are the same length, if the elemnt is smaller than the median, it goes in the
        # small queue.
        # If the heaps aren't the same length, we may have to rebalance.

        m = self.peek()

        if m == None:
            self.h1.insert(new)
        elif new < m: # new goes in small numbers
            if self.h2.length > self.h1.length:
                self.h1.insert(self.h2.pop())
            self.h2.insert(new)
        else:
            if self.h1.length > self.h2.length:
                self.h2.insert(self.h1.pop())
            self.h1.insert(new)            
        

def main():
    m = Median()
    lst = [1,2,3,4,5,6,7,8,9,8,7,6,5]
    for item in lst:
        m.insert(item)

    median = m.peek()
    return median

    
if __name__ == "__main__":
    print(main())
