import pygame
from pygame.sprite import Sprite


class Divider(Sprite):
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.distance_apart = 30
        self.number_of_lines = 10
        self.height = 30
        self.width = 5
        self.rect = pygame.Rect(450, 0 , self.width, self.height)
        self.color = 255, 255, 255


    def draw(self):
        for i in range(0, self.ai_settings.window_height, 60):
            self.rect = pygame.Rect(self.ai_settings.window_width / 2, 0 + i, self.width, self.height)
            pygame.draw.rect(self.screen, self.color, self.rect)
