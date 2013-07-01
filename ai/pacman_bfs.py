#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque


def nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid):
    explored = []
    tmp_stack = deque()
    children_parent = {(pacman_x, pacman_y): (None, None)}
    visisted = set()
    tmp_stack.append((pacman_x, pacman_y))

    while tmp_stack:
        checkpos_x, checkpos_y = tmp_stack.popleft()
        if (checkpos_x, checkpos_y) in visisted:
            continue

        explored.append((checkpos_x, checkpos_y))
        visisted.add((checkpos_x, checkpos_y))

        if grid[checkpos_x][checkpos_y] == '.':
            break

        to_explored = [(checkpos_x - 1, checkpos_y),
                       (checkpos_x, checkpos_y - 1),
                       (checkpos_x, checkpos_y + 1),
                       (checkpos_x + 1, checkpos_y)]
        for next_x, next_y in to_explored:
            if (0 < next_x < x - 1 and
                    0 < next_y < y - 1 and
                    grid[next_x][next_y] != '%'):
                tmp_stack.append((next_x, next_y))
                #Prevent loop
                if (next_x, next_y) not in visisted:
                    children_parent[(next_x, next_y)] = (checkpos_x, checkpos_y)

    print len(explored)
    for line in explored:
        print line[0], line[1]

    #Backtracking
    tmp = (food_x, food_y)
    explored = deque()
    while tmp != (pacman_x, pacman_y):
        explored.append(tmp)
        tmp = children_parent[tmp]

    print len(explored)
    print pacman_x, pacman_y
    while explored:
        line = explored.pop()
        print line[0], line[1]
