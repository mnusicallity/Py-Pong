import pygame
from pygame.sprite import Sprite
import time

class Ball(Sprite):
    def __init__(self, screen, ai_settings, paddle, paddle_two):
        super(Ball, self).__init__()
        self.direction_x = 1
        self.direction_y = 1
        self.screen = screen
        self.ai_settings = ai_settings
        self.paddle = paddle
        self.paddle_two = paddle_two
        self.paddle_two
        self.color = (255,255,255)
        self.startx = 600
        self.starty = 450
        self.rect = pygame.Rect(self.startx, self.starty,  10, 10)
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.ball_speed = self.direction_x + self.direction_y
        self.score_left = 0
        self.score_right = 0

    def move(self):
        """Makes the ball move in one of four direction each at a 45 degree angle to x and y"""
        self.startx += self.direction_x
        self.starty += self.direction_y
        self.rect = pygame.Rect(self.startx, self.starty, 10, 10)
        pygame.draw.rect(self.screen, self.color, self.rect)

        #print("X: %s" % self.startx)
        #print("Y: %s" % self.starty)

    def bounce(self):
        """Defines boundaries for the ball to bounce of of"""
        #for i in range(-5, 40, 5):
        if self.starty > self.paddle.paddle_position and  self.starty <= self.paddle.paddle_position + 40 and self.startx <= 0:    # and self.starty <= paddle.paddle_position + 5 and self.startx <= 10:
            self.direction_x *= -1
        elif self.starty > self.paddle_two.paddle_position  and self.starty <= self.paddle_two.paddle_position + 40 and self.startx >= 880:    # and self.starty <= paddle_two.paddle_position + 5 and self.startx >= 880:
            self.direction_x *= -1
        elif self.starty > self.ai_settings.window_height or self.starty < 0:
            self.direction_y *= -1


    def ball_logic(self):
        """Changes the direction of the ball either by colliding with paddle or bouncing off top and bottom."""
        if self.direction_y > self.direction_x:
            self.ball_speed = abs(self.direction_y + self.direction_x)
            self.direction_y = self.ball_speed - self.direction_x
            self.direction_x = self.ball_speed - self.ball_speed_y
        elif self.direction_y == self.direction_x:
            self.ball_speed = abs(self.direction_x + self.direction_y)
            self.direction_y = self.ball_speed - self.direction_x
            self.direction_x = self.ball_speed - self.direction_y
        else:
            self.ball_speed = abs(self.direction_x - self.direction_y)
            self.direction_y = self.ball_speed - self.direction_x
            self.direciton_x = self.ball_speed - self.direction_y

    def reset(self):
        """"After a player scores put it back in the center"""
        if self.startx > 890:
            time.sleep(1)
            self.startx = 450
            self.starty = 300
            self.score_right +=1
        elif self.startx < 0:
            time.sleep(1)
            self.startx = 450
            self.starty = 300
            self.score_left += 1
