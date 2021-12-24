""" Food module to work with food object """

import random

from snake.constants import Colors
from snake.objects.block import Block
from snake.objects.window import Windows


class Food:
    """ Food class to help create food objects """

    x_pos = y_pos = block_size = 0

    def __init__(self, block: Block, color: Colors):
        """ Set Food object to display on the window

        Arguments:
            block {Block} -- Block object
            color {Colors} -- Color of the food block
        """

        self._block = block
        self.x_axis = Windows.width
        self.y_axis = Windows.height
        self._block.set_block_color(color)

    def random_position(self, snake_size: int):
        """ Create random position for food

        Arguments:
            snake_size {int} -- Size of snake to calculate next position of food
        """

        x = Food._get_axis_value(self.x_axis - snake_size)
        y = Food._get_axis_value(self.y_axis - snake_size)

        Food._update_food_pos(x_pos=x, y_pos=y, block_size=snake_size)

    def create_food(self):
        """ Creates food on display window """

        rect = [Food.x_pos, Food.y_pos, Food.block_size, Food.block_size]
        self._block.set_block_size(rect)

        self._block.create_block()

    @staticmethod
    def _get_axis_value(value: int) -> float:
        """ Create a random value use for display rect object

        Arguments:
            value {int} -- Reference value to get new axis value

        Returns:
            [int] -- Integer axis value
        """

        return round(random.randrange(0, value) / 10.0) * 10.0

    @staticmethod
    def _update_food_pos(**kwargs):
        """ Sets class attributes

        Arguments:
           **kwargs -- Dictionary of class attributes to set
        """

        for key, value in kwargs.items():
            setattr(Food, key, value)
