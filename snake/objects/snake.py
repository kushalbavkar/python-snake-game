""" Snake module to work with snake object """

from snake.constants import Colors
from snake.objects.block import Block


class Snake:
    """ Snake class to help create snake objects """

    def __init__(self, block: Block, color: Colors):
        """ Sets the Snake object with Color and Block properties

        Arguments:
            block {Block} -- Block object
            color {Colors} -- Color of the food block
        """

        self._block = block
        self._block.set_block_color(color)

    def draw(self, snake: list, size: int):
        """ Draws snake on display

        Arguments:
            snake {list} -- List of block positions to create snake
            size {int} -- Block size of snake
        """

        for axis in snake:
            # self._block.set_block_size([axis['x'], axis['y'], size, size])
            # self._block.create_block()
            self._block.set_circle_size((axis['x'], axis['y']), int(size/2))
            self._block.create_circle()
