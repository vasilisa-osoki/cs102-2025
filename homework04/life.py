import pathlib
import random
from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[Cell]
Grid = List[List[int]]


class GameOfLife:
    def __init__(self, size: Tuple[int, int], randomize: bool = True, max_generations: Optional[int] = None) -> None:
        """Инициализация игры Жизнь"""
        self.rows, self.cols = size
        self.prev_generation = self.create_grid(False)
        self.curr_generation = self.create_grid(randomize)
        self.max_generations = max_generations
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        """Создание сетки клеток"""
        grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        """Получение списка соседей для клетки"""
        row, col = cell
        neighbours = []

        # Все возможные направления соседей
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Проверка границ
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                neighbours.append((new_row, new_col))

        return neighbours

    def get_next_generation(self) -> Grid:
        """Получение следующего поколения клеток"""
        new_grid = self.create_grid(False)

        for i in range(self.rows):
            for j in range(self.cols):
                # Подсчет живых соседей
                neighbours = self.get_neighbours((i, j))
                alive_neighbours = sum(self.curr_generation[r][c] for r, c in neighbours)

                # Применение правил игры
                if self.curr_generation[i][j] == 1:
                    if 2 <= alive_neighbours <= 3:
                        new_grid[i][j] = 1
                else:
                    if alive_neighbours == 3:
                        new_grid[i][j] = 1

        return new_grid

    def step(self) -> None:
        """Выполнить один шаг игры"""
        self.prev_generation = [row[:] for row in self.curr_generation]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """Проверка превышения максимального числа поколений"""
        if self.max_generations is None:
            return False
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """Изменяется ли состояние поля"""
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """Создание игры из файла"""
        with open(filename, "r") as f:
            lines = [line.strip() for line in f]

        rows = len(lines)
        cols = len(lines[0])

        game = GameOfLife((rows, cols), randomize=False)

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                game.curr_generation[i][j] = 1 if char == "1" else 0

        return game

    def save(self, filename: pathlib.Path) -> None:
        """Сохранение текущего состояния в файл"""
        with open(filename, "w") as f:
            for row in self.curr_generation:
                line = "".join("1" if cell else "0" for cell in row)
                f.write(line + "\n")
