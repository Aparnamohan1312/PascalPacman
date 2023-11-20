# -*- coding: utf-8 -*-
"""Extra_credit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IYXxhrHADXnmX11NyODC2LPmuxU_C3M0
"""

import time
def dfs_pascals_triangle(triangle, start, goal):
    start_time = time.time()

    stack = [(start, [])]

    while stack:
        current, path = stack.pop()

        if current == goal:
            elapsed_time = time.time() - start_time
            print("Execution Time: {:.6f} seconds".format(elapsed_time))

            return path + [current]

        for dx, dy in [(1, 0), (1, 1)]:
            new_i, new_j = current[0] + dx, current[1] + dy
            if 0 <= new_i < len(triangle) and 0 <= new_j < len(triangle[new_i]):
                new_node = (new_i, new_j)
                new_path = path + [current]
                stack.append((new_node, new_path))
    return None

def main():
    rows = int(input("Enter the number of rows for Pacman Pascal's Triangle Maze: "))
    triangle = generate_pascals_triangle(rows)
    print("\nPacman with Pascal's Triangle Maze")
    print_pascals_triangle_with_pacman(triangle, (0, 0))

    start = (0, 0)
    goal = (rows - 1, len(triangle[-1]) // 2)

    print("\nDFS Path:")
    path = dfs_pascals_triangle(triangle, start, goal)

    if path:
        print(path)
        move_pacman(triangle, path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()

from collections import deque
import time
def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        if i > 0:
            row.append(1)
        triangle.append(row)
    return triangle

def print_pascals_triangle_with_pacman(triangle, pacman_position):
    for i, row in enumerate(triangle):
        line = ""
        for j, value in enumerate(row):
            if (i, j) == pacman_position:
                line += "😃"  # Emoticon representing Pacman
            else:
                line += str(value).center(3)
        print(line.center(len(triangle[-1]) * 3))

def bfs_pascals_triangle(triangle, start, goal):
    queue = deque([(0, 0, [])])

    while queue:
        i, j, path = queue.popleft()

        if (i, j) == goal:
            return path + [(i, j)]

        for dx, dy in [(1, 0), (1, 1)]:
            new_i, new_j = i + dx, j + dy
            if 0 <= new_i < len(triangle) and 0 <= new_j < len(triangle[new_i]):
                queue.append((new_i, new_j, path + [(i, j)]))

    return None

def move_pacman(triangle, path):
    print("\nMoving Pacman:")
    for i, (x, y) in enumerate(path):
        print("Step {}: Pacman is at ({}, {})".format(i + 1, x, y))
        print_pascals_triangle_with_pacman(triangle, (x, y))

def main():
    rows = int(input("Pacman with Pascal's Triangle Maze: "))
    triangle = generate_pascals_triangle(rows)
    print("\nPacman with Pascal's Triangle Maze:")
    print_pascals_triangle_with_pacman(triangle, (0, 0))

    start = (0, 0)
    goal = (rows - 1, len(triangle[-1]) // 2)

    print("\nBFS Path:")
    start_time = time.time()
    path = bfs_pascals_triangle(triangle, start, goal)
    elapsed_time = time.time() - start_time

    if path:
        print(path)
        move_pacman(triangle, path)
    else:
        print("No path found.")
    print("Execution Time: {:.6f} seconds".format(elapsed_time))

if __name__ == "__main__":
    main()