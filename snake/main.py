""" PYGAME - Sample game for learning """

from copy import copy

import pygame

from snake.constants import Colors, Snake, Window
from snake.objects.block import Block
from snake.objects.food import Food
from snake.objects.snake import Snake as Python
from snake.objects.window import Windows


def setup(display: Window, title: Window) -> Windows:
    """ Setup pygame display

    Arguments:
        display {Window} -- Window enum conataining dimensions
        title {Window} -- Title

    Returns:
        Windows -- Windows object
    """
    obj = Windows(display.value)
    obj.set_window_title(title.value)

    return obj


def game_loop():
    """ Runs game loop """

    snake_block = Snake.BLOCK_SIZE.value

    game_over = False
    close_game = False

    x_pos = Windows.width / 2
    y_pos = Windows.height / 2

    x_pos_change = 0
    y_pos_change = 0

    snake_size = []
    snake_length = 1

    FOOD.random_position(snake_block)

    while not game_over:

        while close_game:
            WINDOW.fill(Colors.BLACK)
            WINDOW.display_score(snake_length - 1)
            WINDOW.display_message()
            WINDOW.refresh()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        close_game = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_pos_change = -snake_block
                    y_pos_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_pos_change = snake_block
                    y_pos_change = 0
                elif event.key == pygame.K_UP:
                    y_pos_change = -snake_block
                    x_pos_change = 0
                elif event.key == pygame.K_DOWN:
                    y_pos_change = snake_block
                    x_pos_change = 0

        if x_pos >= Windows.width or x_pos < 0 or y_pos >= Windows.height or y_pos < 0:
            close_game = True

        x_pos += x_pos_change
        y_pos += y_pos_change

        WINDOW.fill(Colors.BLACK)
        FOOD.create_food()

        head = {'x': x_pos, 'y': y_pos}
        snake_size.append(head)

        if len(snake_size) > snake_length:
            del snake_size[0]

        for x in snake_size[:-1]:
            if x == head:
                close_game = True

        SNAKE.draw(snake_size, snake_block)
        WINDOW.display_score(snake_length - 1)
        WINDOW.refresh()

        if x_pos == Food.x_pos and y_pos == Food.y_pos:
            FOOD.random_position(snake_block)
            snake_length += 1

        WINDOW.snake_speed(Snake.SPEED)

    Windows.quit()
    quit()


if __name__ == '__main__':

    WINDOW = setup(Window.MEDIUM_SIZE, Window.TITLE)
    BLOCK = Block(WINDOW)
    FOOD = Food(copy(BLOCK), Colors.GREEN)
    SNAKE = Python(copy(BLOCK), Colors.GRAY)

    game_loop()
