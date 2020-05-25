import sys
import pygame

from copy import copy
from objects.window import Windows
from objects.block import Block
from objects.food import Food
from objects.snake import Snake as Python
from constants import Window, Colors, Snake


def setup(display: Window, title: Window) -> Windows:
    obj = Windows(display.value)
    obj.set_window_title(title.value)
    return obj


def game_loop():
    snake_block = Snake.BLOCK_SIZE.value

    game_over = False
    close_game = False

    x_pos = Windows.width / 2
    y_pos = Windows.height / 2

    x_pos_change = 0
    y_pos_change = 0

    snake_size = []
    snake_length = 1

    food.random_position(snake_block)

    while not game_over:

        while close_game:
            window.fill(Colors.BLACK.value)
            window.display_score(str(snake_length - 1))
            window.display_message()
            window.refresh()

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

        window.fill(Colors.BLACK.value)
        food.create_food()

        head = {'x': x_pos, 'y': y_pos}
        snake_size.append(head)

        if len(snake_size) > snake_length:
            del snake_size[0]

        for x in snake_size[:-1]:
            if x == head:
                close_game = True

        snake.draw(snake_size, snake_block)
        window.display_score(str(snake_length - 1))
        window.refresh()

        if x_pos == Food.x_pos and y_pos == Food.y_pos:
            food.random_position(snake_block)
            snake_length += 1

        window.snake_speed(Snake.SPEED)

    Windows.quit()
    sys.exit()


window = setup(Window.MEDIUM_SIZE, Window.TITLE)
block = Block(window)
food = Food(copy(block), Colors.GREEN)
snake = Python(copy(block), Colors.WHITE)

game_loop()
