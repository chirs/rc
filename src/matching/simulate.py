

import random


class MeetGreet(object):
    def __init__(self, m, w):
        self.m = m
        self.w = w

        


def simulation():

    mg = MeetGreet(new, old)
    mg.match()
    mg.remove(3)
    mg.match()
    mg.remove([4,5])
    mg.match()
    mg.match()
    mg.remove([8,12,20,24])
    mg.match()
    mg.remove([1,2,5,6])
    mg.match()

def create_simulation(steps, element_count):
    # This is not good.
    es = set(range(element_count)) # you know this from new,old...
    removed = set()

    mg = MeetGreet(new, old)    
    
    while steps > 0:
        if random.random() > 5:
            rs = random.randint(1, 4)
            for e in range(rs):
                r = es.pop()
                mg.remove(r)
                removed.add(r)
        else:
            mg.match()


def main():
    simulation1()
    s2 = create_simulation(15, 30)
            
            


if __name__ == "__main__":
    main()
            
