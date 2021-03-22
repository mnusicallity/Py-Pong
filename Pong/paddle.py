import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):
    def __init__(self, screen, ai_settings, player_paddle):
        super(Paddle, self).__init__()
        self.ai_settings = ai_settings
        self.color = ai_settings.paddle_color
        self.paddle_position =  400
        self.paddle_speed = 2
        self.screen = screen
        self.player_paddle = player_paddle
        self.rect = pygame.Rect(self.player_paddle, self.paddle_position, 10, 40)
        self.play_against_ai = False
        self.paddle_moving_up = False
        self.paddle_moving_down = False

    def update(self):
        if self.paddle_moving_up:
            self.paddle_position_up()
        elif self.paddle_moving_down:
            self.paddle_position_down()
        print(self.ai_settings.paddle_position)


    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

#    def update(self, ai_settings):+py setup.
#        if ai_settings.paddle_moving_up == True and ai_settings.paddle_position >= 0:


#        elif ai_settings.paddle_moving_down == True and ai_settings.paddle_position <= ai_settings.window_height:


    def paddle_position_up(self):
        self.rect = pygame.Rect(self.player_paddle, self.paddle_position, 10, 40)
        self.paddle_position -= self.paddle_speed

    def paddle_position_down(self):
        self.rect = pygame.Rect(self.player_paddle, self.paddle_position, 10, 40)
        self.paddle_position += self.paddle_speed



    def against_ai(self, ball):
        """This function requires a condition to be met by selecting something from the Game Menu"""


        if ball.starty <= self.paddle_position:
            self.paddle_position_up()
        elif ball.starty >= self.paddle_position:
            self.paddle_position_down()
