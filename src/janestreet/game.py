

import random


cache = {}
move_cache = {}


def play_round(n, previous=None, player=0):

    opponent = (player + 1) % 2
    
    key = (n, previous)
    if key in cache:
        return cache[key]

    if n <= 9 and n != previous:
        return True
    else:
        possible_moves = [e for e in range(1, 9) if e != previous]
        possible_results = [play_round(n - move, move, opponent) for move in possible_moves]
        winning_moves = [move for (move, result) in zip(possible_moves, possible_results) if result == False]

        if len(winning_moves) == 0:
            if player == 0:
                result = False
            else:
                result = True

        else:
            move = winning_moves[0]
            #move_cache[key] = move
            if player == 0:
                result = True
            else:
                result = False
            

        cache[key] = result
        return result


def reconstruct(n):
    l = []
    previous = None

    while n != 0:
        move = move_cache[(n, previous)]        
        l.append(move)
        n -= move
        previous = move


def main():
    #print(play_round(1, None))
    #print(play_round(4, None))
    #print(play_round(9, None))
    #print(play_round(10, None))
    #print(play_round(11, None))

    #play_round(24, None)
    #print(reconstruct(24))
    
    for e in range(100):
        s = '%s: %s' % (e, play_round(e, None))
        print(s)


if __name__ == "__main__":
    main()
        





