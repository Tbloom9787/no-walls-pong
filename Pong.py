import pygame
from pygame.sprite import Group
import PlayerInputs as PlayerInputs
import Functionality as Functionality
from Settings import Settings
from Scoreboard import GameStats
from Scoreboard import Scoreboard
from Ball import Button
from Ball import Ball
from Paddles import PlayerPaddle
from Paddles import EnemyPaddle

WINDOWWIDTH = 1200
WINDOWHEIGHT = 780
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


def run_game():
    # Initialize pygame
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    # Initialize settings, stats, and scoreboard
    settings = Settings()
    stats = GameStats()
    scoreboard = Scoreboard(settings, screen, stats)
    button = Button(screen, "Play!")
    pygame.display.set_caption("Pong No Walls\t11 POINTS WINS A GAME!".expandtabs(145))

    ball = Ball(screen, settings)

    # Initialize both player and enemy paddles
    player_top = PlayerPaddle(screen, settings, 1, 0)
    player_bottom = PlayerPaddle(screen, settings, 1, 1)
    player_right = PlayerPaddle(screen, settings, 0, 2)

    enemy_top = EnemyPaddle(screen, settings, 1, 0)
    enemy_bottom = EnemyPaddle(screen, settings, 1, 1)
    enemy_left = EnemyPaddle(screen, settings, 0, 2)

    # Set each players paddles into a group
    player_paddles = Group()
    player_paddles.add(player_top)
    player_paddles.add(player_bottom)
    player_paddles.add(player_right)

    enemy_paddles = Group()
    enemy_paddles.add(enemy_top)
    enemy_paddles.add(enemy_bottom)
    enemy_paddles.add(enemy_left)

    # Add them to a total group
    all_paddles = Group()
    all_paddles.add(player_top)
    all_paddles.add(player_bottom)
    all_paddles.add(player_right)
    all_paddles.add(enemy_top)
    all_paddles.add(enemy_bottom)
    all_paddles.add(enemy_left)

    # While Loop - Is true until screen is exited
    while True:
        screen.fill(settings.background_color)

        PlayerInputs.check_events(stats, scoreboard, button, player_paddles)
        Functionality.draw_all(ball, all_paddles)
        scoreboard.display_score()
        if not stats.game_active:
            button.draw_button()
            stats.reset_score()

        if stats.game_active:
            Functionality.update_all(ball, all_paddles, player_paddles, enemy_paddles)
            Functionality.check_point_over(stats, ball, all_paddles, scoreboard)
            button = Button(screen, "Play Again?")

        pygame.display.flip()


def display_message(winner):
    text_font = pygame.font.SysFont('Segoe UI', 50).render(winner + " Won!", False, (255, 255, 255))
    text_rect = text_font.get_rect(center=(WINDOWWIDTH/2, WINDOWHEIGHT/4))

    screen.blit(text_font, text_rect)
    pygame.display.update()


if __name__ == '__main__':
    run_game()
