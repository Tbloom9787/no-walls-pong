class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 780
        self.background_color = (35, 35, 145)

        self.paddle_length = 150
        self.paddle_thickness = 20
        self.paddle_speed = 2.5

        self.enemy_paddle_length = 150
        self.enemy_paddle_thickness = 20
        self.enemy_paddle_speed = 2
        self.enemy_paddle_speed_degradation = 0.0002

        self.ball_size = 15
        self.ball_start_speed = 3
        self.ball_acceleration = 0.000015
        self.ball_angular_velocity = 0.01

        # Enemy speed setting to change difficulty
        self.enemy_speed = 0.1
