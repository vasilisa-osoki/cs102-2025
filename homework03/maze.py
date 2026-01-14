from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(
    grid: List[List[Union[str, int]]], coord: Tuple[int, int]
) -> List[List[Union[str, int]]]:
    """
    Удаляет стену между текущей клеткой и соседней

    """
    x, y = coord
    directions = []
    if y + 2 < len(grid[0]):
        directions.append(('right', (x, y + 2), (x, y + 1)))
    if x - 2 >= 0:
        directions.append(('up', (x - 2, y), (x - 1, y)))
    if directions:
        direction, next_cell, wall_cell = choice(directions)
        grid[wall_cell[0]][wall_cell[1]] = " "
    return grid

    pass


def bin_tree_maze(
    rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:
    """
    Генерирует лабиринт алгоритмом двоичного дерева

    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))
    for cell in empty_cells:
        grid = remove_wall(grid, cell)
    if not random_exit:
        grid[rows - 2][1] = "X"
        grid[1][cols - 2] = "X"
    else:
        exits = []
        while len(exits) < 2:
            side = choice(['top', 'bottom', 'left', 'right'])
            if side == 'top':
                x, y = 0, randint(1, cols - 2)
            elif side == 'bottom':
                x, y = rows - 1, randint(1, cols - 2)
            elif side == 'left':
                x, y = randint(1, rows - 2), 0
            elif
                x, y = randint(1, rows - 2), cols - 1
            if (x, y) not in [(0, 0), (0, cols-1), (rows-1, 0), (rows-1, cols-1)]:
                exits.append((x, y))
                grid[x][y] = "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """
    Находит координаты всех выходов (клеток с 'X')

    """
    exits = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "X":
                exits.append((i, j))
    return exits

    pass


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """

    pass


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    pass


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:

    """
    Проверяет, окружён ли выход стенами (тупик)

    """
    x, y = coord
    rows, cols = len(grid), len(grid[0])
    if (x == 0 or x == rows - 1) and (y == 0 or y == cols - 1):
        count_walls = 0
        if x == 0:
            if grid[x + 1][y] == "■": count_walls += 1
        else:
            if grid[x - 1][y] == "■": count_walls += 1
        
        if y == 0:
            if grid[x][y + 1] == "■": count_walls += 1
        else:
            if grid[x][y - 1] == "■": count_walls += 1
        
        return count_walls >= 2

    if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
        count_walls = 0
        neighbors = []
        if x > 0: neighbors.append((x - 1, y))
        if x < rows - 1: neighbors.append((x + 1, y))
        if y > 0: neighbors.append((x, y - 1))
        if y < cols - 1: neighbors.append((x, y + 1))
        
        for nx, ny in neighbors:
            if grid[nx][ny] == "■":
                count_walls += 1
        
        return count_walls >= 3
    
    return False

    pass


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """

    pass


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
