import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border()

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for r in range(self.life.rows):
            for c in range(self.life.cols):
                ch = "#" if self.life.curr_generation[r][c] == 1 else " "
                screen.addch(r + 1, c + 1, ch)

    def run(self) -> None:
        screen = curses.initscr()
        curses.curs_set(0)
        screen.nodelay(True)
        running = True

        while running and self.life.is_changing and not self.life.is_max_generations_exceeded:
            key = screen.getch()
            if key in (ord("q"), ord("Q")):
                running = False

            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.refresh()

            self.life.step()
            curses.napms(100)

        curses.endwin()
