""" Windows module to work with windows object """

import pygame
from snake.constants import Colors, Font, Snake


class Windows:
    """ Windows class to help create windows objects """

    width = height = 0

    def __init__(self, window: dict):
        """ Sets windows object with screen dimensions

        Arguments:
            window {dict} -- Dictionary contains display size
        """

        pygame.init()
        self._window = window
        self._display = Windows._set_display_mode(window)
        self.your_score = 'Score: {}'
        self.losing_message = 'You Lost! Press C-Play Again or Q-Quit'

        self._update_class_vars(width=window['width'], height=window['height'])

    @staticmethod
    def _set_display_mode(window: dict):
        """ Sets the display with size specified

        Arguments:
            window {dict} -- Dictionary contains display size

        Returns:
            [Surface] -- Returns pygame surface object
        """

        return pygame.display.set_mode((window['width'], window['height']))

    @staticmethod
    def _update_class_vars(**kwargs):
        """ Sets class attributes

        Arguments:
           **kwargs -- Dictionary of class attributes to set
        """

        for key, value in kwargs.items():
            setattr(Windows, key, value)

    def draw_block(self, color: tuple, rect: list):
        """ Draws a block on display

        Arguments:
            color {tuple} -- Color of the block
            rect {list} -- Dimensions of the block
        """

        pygame.draw.rect(self._display, color, rect)

    def draw_circle(self, color: tuple, coordinates: tuple, radius: int):
        """ Draws a circle on display

        Arguments:
            color {tuple} -- Color of the circle
            coordinates {tuple} -- tuple containing coordinates
            radius {int} -- radius of circle
        """

        pygame.draw.circle(self._display, color, coordinates, radius)

    def fill(self, color: Colors):
        """ Fills the display with color

        Arguments:
            color {Colors} -- Color of the display
        """

        self._display.fill(color.value)

    def display_score(self, score: int):
        """ Displays score on the display

        Arguments:
            score {int} -- Score to display
        """

        font = Windows._font(Font.CONSOLAS, 20)
        value = font.render(self.your_score.format(str(score)),
                            True, Colors.BLUE.value)

        self._display.blit(value, [0, 0])

    def display_message(self):
        """ Display message on the display """

        font = Windows._font(Font.BAHNSCHRIFT, 25)
        value = font.render(self.losing_message, True, Colors.RED.value)

        self._display.blit(value, [self.width / 6, self.height / 3])

    @staticmethod
    def _font(font: Font, size: int):
        """ Returns pygame font object for specified Font type

        Arguments:
            font {Font} -- Type of font
            size {int} -- Size of font

        Returns:
            [Font] -- Return pygame font object
        """

        return pygame.font.SysFont(font.value, size)

    @staticmethod
    def set_window_title(title: str):
        """ Sets display window title

        Arguments:
            title {str} -- String value to display as title
        """

        pygame.display.set_caption(title)

    @staticmethod
    def snake_speed(speed: Snake):
        """ Speed of snake game

        Arguments:
            speed {Snake} -- Speed of Snake using Snake object
        """

        pygame.time.Clock().tick(speed.value)

    @staticmethod
    def refresh():
        """ Refreshes the display with changes """

        pygame.display.update()

    @staticmethod
    def quit():
        """ Quits the pygame """

        pygame.quit()
