import pygame
import sys

"""
* check_events() - Handles all of user input which would 
* only be keystrokes and the press of the play button.
"""


def check_events(stats, scoreboard, button, player_paddles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                for paddle in player_paddles:
                    paddle.moving_up = True
            elif event.key == pygame.K_DOWN:
                for paddle in player_paddles:
                    paddle.moving_down = True
            elif event.key == pygame.K_LEFT:
                for paddle in player_paddles:
                    paddle.moving_left = True
            elif event.key == pygame.K_RIGHT:
                for paddle in player_paddles:
                    paddle.moving_right = True
            elif event.key == pygame.K_q:
                sys.exit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                for paddle in player_paddles:
                    paddle.moving_up = False
            elif event.key == pygame.K_DOWN:
                for paddle in player_paddles:
                    paddle.moving_down = False
            elif event.key == pygame.K_LEFT:
                for paddle in player_paddles:
                    paddle.moving_left = False
            elif event.key == pygame.K_RIGHT:
                for paddle in player_paddles:
                    paddle.moving_right = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button.check_play_button(mouse_x, mouse_y, stats, scoreboard)
