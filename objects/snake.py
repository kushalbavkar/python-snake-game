from constants import Colors
from objects.block import Block


class Snake:

    def __init__(self, block: Block, color: Colors):
        self._block = block
        self._block.set_block_color(color)

    def draw(self, snake: list, size: int):
        for axis in snake:
            self._block.set_block_size([axis['x'], axis['y'], size, size])
            self._block.create_block()
