### https://www.janestreet.com/puzzles/current-puzzle/


import random

cache = {}
move_cache = {}

def play_round(n, previous_moves=[None], player=0):

    previous_move = previous_moves[-1]

    key = (n, previous_move, player)

    if key in cache:
        return cache[key]

    if n <= 9 and n != previous_move:

        move = n
        result = True
    else:
        opponent = (player + 1) % 2    

        possible_moves = [e for e in range(1, 10) if e != previous_move]
        possible_results = [play_round(n - move, previous_moves[:] + [move], opponent) for move in possible_moves] # sort of magic.
        winning_moves = [move for (move, result) in zip(possible_moves, possible_results) if result == False]

        if len(winning_moves) == 0:
            move = None
            result = False
        else:
            move = winning_moves[0]
            result = True

    cache[key] = result

    #move_cache[key] = move
    #print(previous_moves)
    
    return result


def reconstruct(n):
    l = []
    previous = None
    player = 0

    while True:
        key = (n, previous, player)
        if key not in move_cache:
            return l

        move = move_cache[key]
        l.append(move)

        if move is None:
            break
        
        n -= move
        previous = move
        player = (player + 1) % 2

    return l


def main():
    #print(play_round(1, None))
    #print(play_round(4, None))
    #print(play_round(9, None))
    #print(play_round(10, None))
    #print(play_round(11, None))

    #n = 17
    #print(play_round(n))
    #print(reconstruct(n))
    #import pdb; pdb.set_trace()

    
    for e in range(100):
        print('%s: %s' % (e, play_round(e)))

        
if __name__ == "__main__":
    main()
        





