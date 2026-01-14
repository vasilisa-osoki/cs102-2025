import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed

        self.width = life.cols * cell_size
        self.height = life.rows * cell_size
        self.screen_size = self.width, self.height

        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Game of Life")

        self.paused = False
        self.running = True

    def draw_lines(self) -> None:
        """Отрисовка сетки"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """Отрисовка клеток"""
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                color = pygame.Color("green") if self.life.curr_generation[i][j] == 1 else pygame.Color("white")
                rect = pygame.Rect(
                    j * self.cell_size,
                    i * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, color, rect)

    def run(self) -> None:
        """Основной цикл игры"""
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.paused = not self.paused
                    elif event.key == K_ESCAPE:
                        self.running = False

                elif event.type == MOUSEBUTTONDOWN and self.paused:
                    x, y = event.pos
                    col = x // self.cell_size
                    row = y // self.cell_size

                    if 0 <= row < self.life.rows and 0 <= col < self.life.cols:
                        self.life.curr_generation[row][col] = 0 if self.life.curr_generation[row][col] == 1 else 1

            self.screen.fill(pygame.Color("white"))
            self.draw_grid()
            self.draw_lines()
            if not self.paused and self.running:
                self.life.step()
                if self.life.is_max_generations_exceeded or not self.life.is_changing:
                    self.running = False
            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()


if __name__ == "__main__":
    life = GameOfLife((48, 64), randomize=True, max_generations=100)
    gui = GUI(life, cell_size=10, speed=10)
    gui.run()
