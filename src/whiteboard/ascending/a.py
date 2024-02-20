


class Ascending(object):

    def __init__(self, lst=None):
        self.stream = []
        self.longest = []

        if lst:
            for n in lst:
                self.add(n)

    def add(self, n):
        filtered = [b for a,b in zip(self.stream, self.longest) if a < n]
        if filtered:
            l = 1 + max(filtered)
        else:
            l = 1
            
        self.stream.append(n)
        self.longest.append(l)

    def get_longest(self):
        return max(self.longest)

    def get_list(self):
        # This doesn't work.
        l = []
        max = 0
        for a, b in zip(self.stream, self.longest):
            if b > max:
                max = b                
                l.append(a)
        return l


def main():
    print(Ascending([3, 5, 7, 8, 9, 11, 13, 16]).get_longest())
    print(Ascending([8, 7, 6, 5, 4, 3, 2, 1, 0]).get_longest())
    a = Ascending([3, 5, 13, 7, 21, 8, 39, 41, 11, 13, 16, 19, 21])
    print(a.longest)
    #print(a.get_longest())
    #print(a.get_list())


if __name__ == "__main__":
    main()



        
        
