#!/usr/bin/python
# coding: utf-8

""" Game of life implementation """
import sys
import re
import itertools

def neighbors(point):
    """ What we have around """
    gol_x, gol_y = point
    for i, j in itertools.product(range(-1, 2), repeat=2):
        if any((i, j)):
            yield (gol_x + i, gol_y + j)

def advance(board, gol_cond_b, gol_cond_s):
    """ Next step. And since only True in the dictionary. Just simply a set of coordinates.
        New state is not needed. We can re-create the list of living cells.
    """
    gol_result_b = False
    gol_result_s = False

    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbors, board)))
    for point in recalc:
        count = sum((neigh in board) for neigh in neighbors(point))
#        print count
#        gol_point = point in board
#        print gol_point
        result_b = map(lambda b: (count == b and not (point in board)) , gol_cond_b)
        result_s = map(lambda s: (count == s and point in board), gol_cond_s)
#        print 'b '
#        print result_b
#        print 's '
#        print result_s
        for cur_b in result_b:
            gol_result_b = gol_result_b or cur_b
#        print gol_result_b
        for cur_s in result_s:
            gol_result_s = gol_result_s or cur_s
#        print gol_result_s
#        if count == 3 or (count == 2 and point in board):
#            newstate.add(point)

        if gol_result_s or gol_result_b:
            newstate.add(point)

        gol_result_b = False
        gol_result_s = False

    return newstate

def gol_read():
    """ Read from stdin  new state """
    gol_i = 0
    gol_j = 0
    for line in sys.stdin:
        result = re.findall(r'^\!', line)
        if result != ['!']:
            gol_i = gol_i + 1
            gol_field_height = gol_i
            for gol_char in line:
                gol_j = gol_j + 1
                if gol_char == 'O':
                    gol_state.add((gol_i, gol_j))
            gol_field_width = gol_j
            gol_j = 0
    return (gol_field_height, gol_field_width)

def gol_print():
    """ Print ASCII to stdout """
    for gol_i in xrange(gol_field_height-1):
        gol_str = ''
        for gol_j in xrange(gol_field_width-1):
            if (gol_i, gol_j) in gol_state:
                gol_str = gol_str + 'O'
            else:
                gol_str = gol_str + '.'
        print gol_str

gol_state = set()
#print gol_state
(gol_field_height, gol_field_width) = gol_read()
#print gol_field_height

for gol_k in range(1):
    gol_state = advance(gol_state, [3,6,8], [2,4,5])
#    print gol_state
    gol_print()
