""" Game of life implementation """
import itertools

def neighbors(point):
    """ What we have around """
    gol_x, gol_y = point
    for i, j in itertools.product(range(-1, 2), repeat=2):
        if any((i, j)):
            yield (gol_x + i, gol_y + j)

def advance(board):
    """ Next step """
    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbors, board)))
    for point in recalc:
        count = sum((neigh in board) for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)

    return newstate

GLIDER = set([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])
for gol_i in range(3):
    GLIDER = advance(GLIDER)
print GLIDER
