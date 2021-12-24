""" Block module to work with block object """

from snake.constants import Colors, Snake
from snake.objects.window import Windows


class Block:
    """ Block class to help create block objects """

    def __init__(self, window: Windows):
        """ Sets block object to draw rectangle on display

        Arguments:
            window {Windows} -- Windows object
        """

        self._window = window
        self._color = Colors.BLACK.value
        self._rect = Snake.RECT_SIZE.value
        self._circle = Snake.CIRCLE_SIZE.value

    def create_block(self):
        """ Creates block on display"""

        self._window.draw_block(self._color, self._rect)

    def create_circle(self):
        """ Creates circle on display"""

        coordinates, radius = self._circle
        self._window.draw_circle(self._color, coordinates, radius)

    def set_block_color(self, color: Colors):
        """ Sets block color using specified Color value

        Arguments:
            color {Colors} -- Enum object of Colors
        """

        self._color = color.value

    def set_block_size(self, rect: list):
        """ Sets the size of block using the dimensions

        Arguments:
            rect {list} -- list object containing dimensions
        """

        self._rect = rect

    def set_circle_size(self, coordinates: tuple, radius: int):
        """ Sets the size of circle using the dimensions

        Arguments:
            coordinates {tuple} -- tuple containing coordinates
            radius {int} -- radius of circle
        """

        self._circle = coordinates, radius
