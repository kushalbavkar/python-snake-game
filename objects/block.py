from constants import Colors, Snake
from objects.window import Windows


class Block:

    def __init__(self, window: Windows):
        """ Sets block object to draw rectangle on display

        Arguments:
            window {Windows} -- Windows object
        """
        self._window = window
        self._color = Colors.BLACK.value
        self._rect = Snake.RECT_SIZE.value

    def create_block(self):
        """ Creates rectange on display"""
        self._window.draw_block(self._color, self._rect)

    def set_block_color(self, color: Colors):
        """ Sets block color using specified Color value

        Arguments:
            color {tuple} -- tuple containing color values
        """
        self._color = color.value

    def set_block_size(self, rect: list):
        """ Sets the size of block using the dimensions

        Arguments:
            rect {list} -- list object containing dimensions
        """
        self._rect = rect
