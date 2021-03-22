import pygame
from pygame.locals import *
import time
from paddle import Paddle
from settings import Settings
import sys

class VsPaddle():
    def __init__(self, paddle, screen):
        self.paddle = paddle
        self.screen = screen
        self.paddle.color = (255, 255, 255)
        self.paddle.position = 100
        self.paddle.draw_paddle()




    def test_screen(self):
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            self.first_shot()

    def first_shot(self):
        if self.paddle.position < 400:
            self.paddle.position += 1

ai_setting = Settings()
screen = pygame.display.set_mode((900, 600))
paddle = Paddle(screen, ai_setting, 590)
ai = VsPaddle(paddle, screen)

ai.test_screen()