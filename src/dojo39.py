
vowels = set('aeiou')
consonants = set('bcdfghjklmnpqrstvwxz')


def mp(length):
    if length == 1:
        for e in vowels.union(consonants):
            yield e
    else:
        pw1 = mp(length-1)
        for pw in pw1:
            if pw[0] in vowels:
                ls = consonants
            else:
                ls = vowels
            for l in ls:
                yield l + pw

if __name__ == "__main__":
    #for e in mp(3):
    #    print(e)
    print(len([e for e in mp(6)]))
            
            
                
