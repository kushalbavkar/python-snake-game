""" Contants module help define constants required for game """

from enum import Enum


class Window(Enum):
    """ Window enum with display window specifications """

    DEFAULT_SIZE = {'width': 400, 'height': 300}
    MEDIUM_SIZE = {'width': 600, 'height': 400}
    TITLE = 'First python game - Snake!'


class Colors(Enum):
    """ Colors enum with color specifications """

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (50, 153, 213)
    YELLOW = (255, 255, 102)
    GRAY = (96, 96, 96)


class Snake(Enum):
    """ Snake enum with snake specifications """

    BLOCK_SIZE = 10
    SPEED = 15
    RECT_SIZE = (30, 30, 60, 60)


class Font(Enum):
    """ Font enum with font specifications """

    BAHNSCHRIFT = 'bahnschrift'
    CONSOLAS = 'consolas'
