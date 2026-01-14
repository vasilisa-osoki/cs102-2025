import curses
import time
from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.screen = None

    def draw_borders(self, screen) -> None:
        """Отрисовка рамки"""
        height, width = screen.getmaxyx()
        screen.addstr(0, 0, '+' + '-' * (width - 2) + '+')
        screen.addstr(height - 1, 0, '+' + '-' * (width - 2) + '+')
        for i in range(1, height - 1):
            screen.addstr(i, 0, '|')
            screen.addstr(i, width - 1, '|')

    def draw_grid(self, screen) -> None:
        """Отрисовка клеток"""
        height, width = screen.getmaxyx()
        for i in range(1, height - 1):
            if i - 1 < self.life.rows:
                line = ''
                for j in range(1, width - 1):
                    if j - 1 < self.life.cols:
                        cell = self.life.curr_generation[i - 1][j - 1]
                        line += 'O' if cell == 1 else ' '
                    else:
                        break
                screen.addstr(i, 1, line)
            else:
                break

    def run(self) -> None:
        """Основной цикл консольной версии"""
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        curses.curs_set(0)
        
        try:
            self.screen.timeout(100)
            
            running = True
            while running:
                self.screen.clear()
                height, width = self.screen.getmaxyx()
                self.draw_borders(self.screen)
                self.draw_grid(self.screen)
                info = f"Generation: {self.life.generations} | Press 'q' to quit"
                if width > len(info):
                    self.screen.addstr(height - 2, 2, info)
                self.screen.refresh()
                key = self.screen.getch()
                if key == ord('q') or key == ord('Q'):
                    running = False
                self.life.step()
                if (self.life.is_max_generations_exceeded 
                        or not self.life.is_changing):
                    running = False
                time.sleep(0.1)
        
        finally:
            curses.nocbreak()
            self.screen.keypad(False)
            curses.echo()
            curses.endwin()


if __name__ == '__main__':
    life = GameOfLife((20, 40), randomize=True, max_generations=50)
    console = Console(life)
    console.run()
