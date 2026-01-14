import pygame
from pygame.locals import *
import random


class GameOfLife:
    def __init__(
        self, 
        width: int = 640, 
        height: int = 480, 
        cell_size: int = 10, 
        speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.speed = speed
        
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        
        self.screen_size = width, height
        self.screen = None
        self.grid = None

    def create_grid(self, randomize: bool = False):
        """Создание сетки"""
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
            pygame.draw.line(
                self.screen, 
                pygame.Color('black'), 
                (x, 0), 
                (x, self.height)
            )
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, 
                pygame.Color('black'), 
                (0, y), 
                (self.width, y)
            )

    def draw_grid(self) -> None:
        """Рисование клеток"""
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j] == 1:
                    color = pygame.Color('green')
                else:
                    color = pygame.Color('white')
                
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        j * self.cell_size,
                        i * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )
                )

    def get_neighbours(self, cell):
        """Получение соседей (упрощенная версия)"""
        row, col = cell
        neighbours = []
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if (0 <= new_row < self.cell_height and 
                        0 <= new_col < self.cell_width):
                    neighbours.append(self.grid[new_row][new_col])
        
        return neighbours

    def get_next_generation(self):
        """Следующее поколение"""
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
        pygame.display.set_caption('Game of Life - Prototype')
        
        clock = pygame.time.Clock()
        self.grid = self.create_grid(randomize=True)
        
        running = True
            
            self.screen.fill(pygame.Color('white'))
            
            self.draw_grid()
            self.draw_lines()
            self.grid = self.get_next_generation()
            
            pygame.display.flip()
            clock.tick(self.speed)
        
        pygame.quit()


if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

