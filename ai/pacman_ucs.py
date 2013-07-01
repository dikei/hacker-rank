#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq


def ucs(pacman_x, pacman_y, food_x, food_y, size_x, size_y, matrix):
    queue = [(0, pacman_x, pacman_y)]
    parent = {}
    while len(queue) > 0:
        cost, item_x, item_y = heapq.heappop(queue)

        if item_x == food_x and item_y == food_y:
            print cost
            counter = 0
            current_item = (item_x, item_y)
            tmp = []
            while counter < cost:
                current_item = parent[current_item]
                if current_item[0] == food_x and current_item[1] == food_y:
                    break
                tmp.append(current_item)
                counter += 1
            for row in reversed(tmp):
                print row[0], row[1]
            print food_x, food_y
            break

        #Check up
        up_x, up_y = item_x - 1, item_y
        if ((up_x, up_y) not in parent and
                up_x >= 0 and
                matrix[up_x][up_y] != '%'):
            heapq.heappush(queue, (cost + 1, up_x, up_y))
            parent[(up_x, up_y)] = (item_x, item_y)

        #Check down
        down_x, down_y = item_x + 1, item_y
        if ((down_x, down_y) not in parent and
                down_x < size_x and
                matrix[down_x][down_y] != '%'):
            heapq.heappush(queue, (cost + 1, down_x, down_y))
            parent[(down_x, down_y)] = (item_x, item_y)

        #Check left
        left_x, left_y = item_x, item_y - 1
        if ((left_x, left_y) not in parent and
                left_y >= 0 and
                matrix[left_x][left_y] != '%'):
            heapq.heappush(queue, (cost + 1, left_x, left_y))
            parent[(left_x, left_y)] = (item_x, item_y)

        #Check right
        right_x, right_y = item_x, item_y + 1
        if ((right_x, right_y) not in parent and
                right_y < size_y and
                matrix[right_x][right_y] != '%'):
            heapq.heappush(queue, (cost + 1, right_x, right_y))
            parent[(right_x, right_y)] = (item_x, item_y)

if __name__ == "__main__":
    pacman_x, pacman_y = [int(i) for i in raw_input().split()]
    food_x, food_y = [int(i) for i in raw_input().split()]
    size_x, size_y = [int(i) for i in raw_input().split()]
    matrix = []

    for i in range(0, size_y):
        matrix.append(list(raw_input()))

    ucs(pacman_x, pacman_y, food_x, food_y, size_x, size_y, matrix)
