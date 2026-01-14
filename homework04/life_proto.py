import random

import pygame
from pygame.locals import *


class GameOfLife:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.speed = speed

        # Вычисляем количество клеток
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Создаем окно
        self.screen_size = width, height
        self.screen = None
        self.grid = None

    def create_grid(self, randomize: bool = False):
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        grid = []
        for i in range(self.cell_height):
            row = []
            for j in range(self.cell_width):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def draw_lines(self) -> None:
        """Рисование сетки"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j] == 1:
                    color = pygame.Color("green")
                else:
                    color = pygame.Color("white")

                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        j * self.cell_size,
                        i * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )

    def get_neighbours(self, cell):
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток, в котором каждая позиция – 0 или 1.
        """
        row, col = cell
        neighbours = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if 0 <= new_row < self.cell_height and 0 <= new_col < self.cell_width:
                    neighbours.append(self.grid[new_row][new_col])

        return neighbours

    def get_next_generation(self):
        """
        Получить следующее поколение клеток.
        """
        new_grid = self.create_grid(False)

        for i in range(self.cell_height):
            for j in range(self.cell_width):
                neighbours = self.get_neighbours((i, j))
                alive_neighbours = sum(neighbours)

                if self.grid[i][j] == 1:
                    if 2 <= alive_neighbours <= 3:
                        new_grid[i][j] = 1
                else:
                    if alive_neighbours == 3:
                        new_grid[i][j] = 1

        return new_grid

    def run(self) -> None:
        """Запуск игры"""
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Game of Life - Prototype")

        clock = pygame.time.Clock()
        self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Очищаем экран
            self.screen.fill(pygame.Color("white"))

            # Отрисовываем и обновляем
            self.draw_grid()
            self.draw_lines()
            self.grid = self.get_next_generation()

            # Обновляем экран
            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()


if __name__ == "__main__":
    game = GameOfLife(320, 240, 20)
    game.run()
