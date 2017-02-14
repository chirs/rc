"""
Improving the RC algorithm for meet and greets

What's wrong with meet and greets? I was matched with Mel and Jay today. I propose that new people should be matched with more experienced people. [objections? alternatives?]

Current strategy:
Unclear, but can't separate people by batch.

New strategy:
Assume that there are more old people than new people (old: seconds, alums, staff) [questionable]
Separate lists into old and new
Equalize the length of the two lists
Match 1-1, with a shift if necessary. This covers the entire matching space clearly and quickly.

Other strategies:
Pull randomly from bags and backtrack if necessary.

Bugs: 
Does not satisfy Nick's requirement that people can enter and leave arbitrarily
Does not fail gracefully

Features:
Intelligent pair (edge?) swapping
Neural network
Graph problem
"""

# Follow my strategy
# And gracefully degrade when adding / dropping people
# Presumably only removing, right?
# Match non-conforming pairs after shift generation.
# Verify by simulation that this strategy is appropriate.
# Pair scoring

import random

def equalize_lengths(l1, l2):
    """
    Make l1 and l2 approximately equal
    """
    # If there are an odd number of total elements,
    # the initially longer list will be longer by 1 element

    ld = len(l1) - len(l2)
    diff = int(ld/2)
    
    if diff < 0:
        m1 = l1 + l2[diff:]
        m2 = l2[:diff]

    elif diff > 0:

        m1 = l1[:-diff]
        m2 = l2 + l1[-diff:]
    else:
        m1 = l1[:]
        m2 = l2[:]

    return (m1, m2)


def get_extra(l1, l2):
    """
    Return the extra element from the end of the longer list.
    """
    d = len(l1) - len(l2)
    if d == 0:
        return None
    elif d == 1:
        return l1[-1]
    else:
        return l2[-1]
        
        
def match(l1, l2, seen, shift=0):
    """
    Match two lists.
    Returns None, None if previous pairs are not avoided
    """

    m1, m2 = equalize_lengths(l1, l2)

    #random.shuffle(m1)
    ls = lambda l, shift: l[shift:] + l[:shift] # linear shift instead
    
    ts = [tuple(sorted([a,b])) for (a,b) in zip(ls(m1, shift), m2)] # Construct pairs

    # Guard against any duplicates
    # (Stupidly)
    new_seen = seen.copy()    
    for t in ts: 
        if t in seen:
            return None, None

        new_seen.add(t)

    return (ts, new_seen)


def swap(pairs, new_entries, seen_pairs):
    # Who cares this never happens.
    pairs = zip(new_entries[::2], entries[1::2]) # last new entry will be dropped.

def unmatch(pairs, removed):
    ps = []
    rs = set(removed)
    unpaired = []
    for pair in pairs:
        a, b = pair
        if a in rs:
            unpaired.append(b)
        if b in rs:
            unpaired.append(a)
        if a not in rs and b not in rs: 
            ps.append(pair)

    return (ps, unpaired)


def unmatcher(people):
    l = []
    THRESHOLD = .01
    for e in people:
        if random.random() < THRESHOLD:
            l.append(e)
    return l


def split(l):
    d = int(len(l) / 2)
    return l[:d], l[d:]


def main():
    """
    """
    old_people = range(0, 35)
    new_people = range(35, 60)
    people = set(old_people + new_people)
    seen_pairs = set()

    exiters = set()

    for e in range(30):
        pairs, new_seen = match(new_people, old_people, seen_pairs, e)

        exiters.update(unmatcher(people))

        if new_seen is None:
            print("")
        else:
            print(len(seen_pairs))
            seen_pairs = new_seen

        good_pairs, unpaired = unmatch(pairs, exiters)
        print(unpaired)
        r1, r2 = split(unpaired)
        pairs, new_seen = match(r1, r2, seen_pairs, e) # new, additive match function here.
        #final_pairs, seen_pairs, success = match_insert(unpaired, good_pairs, seen_pairs)
        


def test():
    old_people = range(0, 35)
    new_people = range(35, 60)
    seen_pairs = set()

    l1, l2 = equalize_lengths(new_people, old_people)
    print(len(l1))
    print(len(l2))

    l1, l2 = equalize_lengths(old_people, new_people)
    print(len(l1))
    print(len(l2))

    

if __name__ == "__main__":
    main()

                   
