import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed

        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.paused = False

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                color = (
                    pygame.Color("green")
                    if self.life.curr_generation[row][col] == 1
                    else pygame.Color("white")
                )
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN and event.key == K_SPACE:
                    self.paused = not self.paused
                if self.paused and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    col = x // self.cell_size
                    row = y // self.cell_size
                    if 0 <= row < self.life.rows and 0 <= col < self.life.cols:
                        self.life.curr_generation[row][col] = (
                            0 if self.life.curr_generation[row][col] == 1 else 1
                        )

            self.screen.fill(pygame.Color("white"))
            self.draw_grid()
            self.draw_lines()

            if (
                not self.paused
                and self.life.is_changing
                and not self.life.is_max_generations_exceeded
            ):
                self.life.step()

            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()
game=GameOfLife(size=(80, 60))
ui=GUI(game)
ui.run()
