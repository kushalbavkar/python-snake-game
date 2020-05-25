import pygame
from constants import Colors, Font, Snake


class Windows:
    width = height = 0

    def __init__(self, window: dict):
        pygame.init()
        self._window = window
        self._display = Windows._set_display_mode(window)
        self._update_class_vars()
        self.your_score = 'Your Score: {}'
        self.losing_message = 'You Lost! Press C-Play Again or Q-Quit'

    @staticmethod
    def _set_display_mode(window: dict):
        return pygame.display.set_mode((window['width'], window['height']))

    def _update_class_vars(self):
        setattr(Windows, 'width', self._window['width'])
        setattr(Windows, 'height', self._window['height'])

    def draw_block(self, color: tuple, rect: list):
        pygame.draw.rect(self._display, color, rect)

    def fill(self, color: tuple):
        self._display.fill(color)

    def display_score(self, score: str):
        font = Windows.font(Font.COMIC_SANS, 35)
        value = font.render(self.your_score.format(score),
                            True, Colors.YELLOW.value)
        self._display.blit(value, [0, 0])

    def display_message(self):
        font = Windows.font(Font.BAHNSCHRIFT, 25)
        value = font.render(self.losing_message, True, Colors.RED.value)
        self._display.blit(value, [self.width / 6, self.height / 3])

    @staticmethod
    def font(font: Font, size: int):
        return pygame.font.SysFont(font.value, size)

    @staticmethod
    def set_window_title(title: str):
        pygame.display.set_caption(title)

    @staticmethod
    def snake_speed(speed: Snake):
        pygame.time.Clock().tick(speed.value)

    @staticmethod
    def refresh():
        pygame.display.update()

    @staticmethod
    def quit():
        pygame.quit()
