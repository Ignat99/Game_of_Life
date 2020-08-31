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

def advance(board):
    """ Next step """
    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbors, board)))
    for point in recalc:
        count = sum((neigh in board) for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)

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
    for gol_i in xrange(gol_field_height):
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

for gol_k in range(1):
    gol_state = advance(gol_state)
#    print gol_state
    gol_print()
