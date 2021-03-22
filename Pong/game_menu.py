__author__ =  'Conor Hamilton'

import pygame.font


class GameMenu():
    def __init__(self, screen, ai_settings):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.menu_selection = ["Two Player", "One Player", "Difficulty"]
        self.difficulty_setting = ['Easy', 'Medium', 'Hard']
        self.menu_option_color = (0, 255, 0)
        self.menu_background_color = (30,30,30)
        self.menu_option_width = 200
        self.menu_option_height = 50
        self.font = pygame.font.SysFont(None, 24)
        self.rect = pygame.Rect(0, 0, self.menu_option_width, self.menu_option_height)
        self.menu_rect = pygame.Rect(0,0, self.menu_option_width, self.menu_option_height)
        self.rect.center = self.screen_rect.center
        self.menu_rect.center =  self.screen_rect.center
        self.menu_rect.top += 100
        self.rect.top += 50
        self.selection = 0
        self.select_difficulty = False


    def game_menu(self):
        """Creates menu beneath play button that can be navigated using the left and right arrows"""
        if not self.select_difficulty:
            self.menu_option = self.font.render(self.menu_selection[self.selection], True, self.menu_option_color, self.menu_background_color)
            self.menu_option_rect = self.menu_option.get_rect()
            self.menu_option_rect.center = self.rect.center
            self.screen.fill(self.menu_background_color, self.rect)
            self.screen.blit(self.menu_option, self.menu_option_rect)
        else:
            self.menu_option = self.font.render("Difficulty", True, self.menu_option_color, self.menu_background_color)
            self.menu_option_rect = self.menu_option.get_rect()
            self.menu_option_rect.center = self.rect.center
            self.screen.fill(self.menu_background_color, self.rect)
            self.screen.blit(self.menu_option, self.menu_option_rect)


    def dropdown_menu_for_difficulty_settings(self):

        self.difficulty_settings = self.font.render(self.difficulty_setting[self.selection], True, self.menu_option_color, self.menu_background_color)
        self.difficulty_settings_rect = self.difficulty_settings.get_rect()
        self.difficulty_settings_rect.center = self.menu_rect.center
        self.screen.fill(self.menu_background_color, self.menu_rect)
        self.screen.blit(self.difficulty_settings, self.difficulty_settings_rect)
        

    def nav(self):
        self.right_arrow = pygame.image.load('Images/right arrow.png')
        self.right_arrow_rect = self.right_arrow.get_rect()
        self.right_arrow_rect.x = 560
        if not self.select_difficulty:
            self.right_arrow_rect.y = 315
        else:
            self.right_arrow_rect.y = 365
        self.screen.blit(self.right_arrow, self.right_arrow_rect)
        self.left_arrow = pygame.image.load('Images/left arrow.png')
        self.left_arrow_rect = self.left_arrow.get_rect()
        self.left_arrow_rect.x = 295
        if not self.select_difficulty:
            self.left_arrow_rect.y = 315
        else:
            self.left_arrow_rect.y = 365
        self.screen.blit(self.left_arrow, self.left_arrow_rect)


