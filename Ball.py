import pygame
import random
import pygame.font
from pygame.sprite import Sprite

"""
* class Ball - Controls the ball functionality
* and collision into paddles or a wall. Collision
* requires the change in velocity of the ball for
* realistic rebound effects. 

* class Button - Creates a general button that is
* able to be clicked and display any message.
"""


class Ball(Sprite):
    def __init__(self, screen, settings):
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(0, 0, settings.ball_size, settings.ball_size)
        self.rect.center = self.screen_rect.center

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.ball_start_speed = settings.ball_start_speed
        self.ball_acceleration = settings.ball_acceleration
        self.ball_angular_velocity = settings.ball_angular_velocity
        self.ball_sound = pygame.mixer.Sound('Sounds/Beep1.wav')

        rand_velocity = random.uniform(-self.ball_start_speed, self.ball_start_speed)
        self.velocity_x = rand_velocity
        self.velocity_y = self.ball_start_speed - abs(rand_velocity)

        self.last_paddle_collided_with = None

    def update(self, paddles):
        self.velocity_x += self.ball_acceleration if self.velocity_x > 0 else -self.ball_acceleration
        self.centerx += self.velocity_x
        self.rect.centerx = self.centerx

        collision = pygame.sprite.spritecollideany(self, paddles)
        self.horizontal_collision(collision)

        self.velocity_y += self.ball_acceleration if self.velocity_y > 0 else -self.ball_acceleration
        self.centery += self.velocity_y
        self.rect.centery = self.centery

        collision = pygame.sprite.spritecollideany(self, paddles)
        self.vertical_collision(collision)

    def vertical_collision(self, collision):
        if collision:
            if collision != self.last_paddle_collided_with:
                self.last_paddle_collided_with = collision
                self.velocity_y *= -1
                difference = self.rect.centerx - collision.rect.centerx
                velocity_change_amount = difference * self.ball_angular_velocity
                self.velocity_x += velocity_change_amount
                self.ball_sound.play()

    def horizontal_collision(self, collision):
        if collision:
            if collision != self.last_paddle_collided_with:
                self.last_paddle_collided_with = collision
                self.velocity_x *= -1
                difference = self.rect.centery - collision.rect.centery
                velocity_change_amount = difference * self.ball_angular_velocity
                self.velocity_y += velocity_change_amount
                self.ball_sound.play()

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.rect.center, self.rect.width)

    def reset(self):
        rand_vel = random.uniform(-self.ball_start_speed, self.ball_start_speed)
        self.velocity_x = rand_vel
        self.velocity_y = self.ball_start_speed - rand_vel
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery
        self.last_paddle_collided_with = None


class Button:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 175, 70
        self.button_color = (40, 225, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Segoe UI', 50)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_play_button(self, mouse_x, mouse_y, stats, scoreboard):
        button_clicked = self.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not stats.game_active:
            stats.player_score = 0
            stats.enemy_score = 0
            scoreboard.initialize_score_display()
            stats.game_active = True
