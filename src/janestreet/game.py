### https://www.janestreet.com/puzzles/current-puzzle/

cache = {} # A cache mapping (n, previous_move, player) -> result

def play_round(n, previous_moves=[], player=0):

    opponent = (player + 1) % 2                    
    
    if previous_moves == []:
        previous_moves = [] # Avoid mutating list
        previous_move = None
    else:
        previous_move = previous_moves[-1]

    key = (n, previous_move, player)

    if key in cache:        
        return cache[key]

    if n <= 9 and n != previous_move:
        move = n
        result = True
    else:
        # Minimax?
        possible_moves = [e for e in range(1, 10) if e != previous_move]
        # sort of magic...recurse into all possibile futures. what's this called?
        possible_results = [play_round(n - move, previous_moves[:] + [move], opponent) for move in possible_moves] 
        winning_moves = [move for (move, result) in zip(possible_moves, possible_results) if result == False]

        if len(winning_moves) == 0:
            move = None
            result = False
        else:
            move = winning_moves[0]
            result = True

    cache[key] = result
    return result #, moves?


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

    s = set()
    l = []
    for e in range(10000):
        # print('%s: %s' % (e, play_round(e)))
        if not play_round(e):
            s.add(e % 32)
    print(s)
        
if __name__ == "__main__":
    main()
        





