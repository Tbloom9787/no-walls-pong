import pygame
from pygame.sprite import Sprite

"""
* Both the paddle classes are very similar and they handle
* the display, position, and movement.
"""


class PlayerPaddle(Sprite):
    def __init__(self, screen, settings, direction, side):
        super(PlayerPaddle, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.paddle_speed = settings.paddle_speed
        self.direction = direction
        self.side = side

        if direction == 0:
            self.rect = pygame.Rect(0, 0, settings.paddle_thickness, settings.paddle_length)
        else:
            self.rect = pygame.Rect(0, 0, settings.paddle_length, settings.paddle_thickness)

        if side == 0:
            self.rect.centerx = self.screen_rect.centerx * 1.5
            self.rect.top = self.screen_rect.top
        elif side == 1:
            self.rect.centerx = self.screen_rect.centerx * 1.5
            self.rect.bottom = self.screen_rect.bottom
        elif side == 2:
            self.rect.right = self.screen_rect.right
            self.rect.centery = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.direction == 0:
            if self.moving_up and self.rect.y > self.screen_rect.top:
                self.centery -= self.paddle_speed
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.centery += self.paddle_speed

        elif self.direction == 1:
            if self.moving_left and self.rect.left > self.screen_rect.centerx:
                self.centerx -= self.paddle_speed
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.centerx += self.paddle_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def draw(self):
        pygame.draw.rect(self.screen, (40, 225, 0), self.rect)
        pygame.draw.line(self.screen, (255, 255, 255), [self.screen_rect.centerx, self.screen_rect.top],
                         [self.screen_rect.centerx, self.screen_rect.bottom], 5)

    def reset(self):
        if self.side == 0:
            self.rect.centerx = self.screen_rect.centerx * 1.5
            self.rect.top = self.screen_rect.top
        elif self.side == 1:
            self.rect.centerx = self.screen_rect.centerx * 1.5
            self.rect.bottom = self.screen_rect.bottom
        elif self.side == 2:
            self.rect.right = self.screen_rect.right
            self.rect.centery = self.screen_rect.centery

        self.centerx = self.rect.centerx
        self.centery = self.rect.centery


class EnemyPaddle(Sprite):
    def __init__(self, screen, settings, direction, side):
        super(EnemyPaddle, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.enemy_paddle_max_speed = settings.enemy_paddle_speed
        self.enemy_paddle_speed = settings.enemy_paddle_speed
        self.enemy_paddle_speed_degradation = settings.enemy_paddle_speed_degradation
        self.direction = direction
        self.side = side

        if direction == 0:
            self.rect = pygame.Rect(0, 0, settings.paddle_thickness, settings.paddle_length)
        else:
            self.rect = pygame.Rect(0, 0, settings.paddle_length, settings.paddle_thickness)

        if side == 0:
            self.rect.centerx = self.screen_rect.centerx * 0.5
            self.rect.top = self.screen_rect.top
        elif side == 1:
            self.rect.centerx = self.screen_rect.centerx * 0.5
            self.rect.bottom = self.screen_rect.bottom
        elif side == 2:
            self.rect.left = self.screen_rect.left
            self.rect.centery = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self, ball):
        if self.direction == 0:
            if ball.rect.centery > self.centery and self.rect.bottom < self.screen_rect.bottom:
                self.centery += self.enemy_paddle_speed
            elif ball.rect.centery < self.centery and self.rect.top > self.screen_rect.top:
                self.centery -= self.enemy_paddle_speed

        elif self.direction == 1:
            if ball.rect.centerx > self.centerx and self.rect.right < self.screen_rect.centerx:
                self.centerx += self.enemy_paddle_speed
            elif ball.rect.centerx < self.centerx and self.rect.left > self.screen_rect.left:
                self.centerx -= self.enemy_paddle_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        if self.enemy_paddle_speed > 0.1:
            self.enemy_paddle_speed -= self.enemy_paddle_speed_degradation
        else:
            self.enemy_paddle_speed = 0.1

    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), self.rect)

    def reset(self):
        if self.side == 0:
            self.rect.centerx = self.screen_rect.centerx * 0.5
            self.rect.top = self.screen_rect.top
        elif self.side == 1:
            self.rect.centerx = self.screen_rect.centerx * 0.5
            self.rect.bottom = self.screen_rect.bottom
        elif self.side == 2:
            self.rect.left = self.screen_rect.left
            self.rect.centery = self.screen_rect.centery

        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.enemy_paddle_speed = self.enemy_paddle_max_speed
