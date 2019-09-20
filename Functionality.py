import pygame

"""
* Checks for the arithmetic of winning points,
* games, and the match.
"""


def check_point_over(stats, ball, paddles, scoreboard):
    # Ball hits players middle wall
    if ball.rect.left > ball.screen_rect.right:
        stats.enemy_score += 1
        check_win(stats)
        reset_objects(scoreboard, ball, paddles)

    # Ball hits enemy middle wall
    elif ball.rect.right < ball.screen_rect.left:
        stats.player_score += 1
        check_win(stats)
        reset_objects(scoreboard, ball, paddles)

    elif ball.rect.bottom < ball.screen_rect.top or ball.rect.top > ball.screen_rect.bottom:
        # Ball hits players top or bottom walls
        if ball.rect.centerx > ball.screen_rect.centerx:
            stats.enemy_score += 1
            check_win(stats)
            reset_objects(scoreboard, ball, paddles)

        # Ball hits enemy top or bottom walls
        else:
            stats.player_score += 1
            check_win(stats)
            reset_objects(scoreboard, ball, paddles)


def reset_objects(scoreboard, ball, paddles):
    scoreboard.initialize_score_display()
    ball.reset()
    for paddle in paddles:
        paddle.reset()


def check_win(stats):
    # Sound files to play if a game or match is lost/won
    player_lose_wav = pygame.mixer.Sound('Sounds/YouLose.ogg')
    player_win_wav = pygame.mixer.Sound('Sounds/YouWin.ogg')
    player_wingame_wav = pygame.mixer.Sound('Sounds/MarioWin.ogg')
    player_losegame_wav = pygame.mixer.Sound('Sounds/MarioLose.ogg')

    if stats.player_score >= 11 and stats.player_score >= (stats.enemy_score + 2):
        stats.player_wins += 1
        stats.player_score = 0
        stats.enemy_score = 0
        player_win_wav.play(0)
    elif stats.enemy_score >= 11 and stats.enemy_score >= (stats.player_score + 2):
        stats.enemy_wins += 1
        stats.player_score = 0
        stats.enemy_score = 0
        player_lose_wav.play(0)

    if stats.player_wins >= 3 and stats.player_wins >= (stats.enemy_wins + 2):
        stats.game_active = False
        stats.play_again = True
        player_wingame_wav.play(2)

    elif stats.enemy_wins >= 3 and stats.enemy_wins >= (stats.player_wins + 2):
        stats.game_active = False
        stats.play_again = True
        player_losegame_wav.play(0)


def update_all(ball, all_paddles, player_paddles, enemy_paddles):
    ball.update(all_paddles)
    for paddle in player_paddles:
        paddle.update()
    for paddle in enemy_paddles:
        paddle.update(ball)


def draw_all(ball, all_paddles):
    ball.draw()
    for paddle in all_paddles:
        paddle.draw()
