import pygame.font

class GameStats():
    """Track statistics of Pong"""
    def __init__(self, ai_settings, screen, ball):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
#        self.reset_stats()
        self.font = pygame.font.SysFont(None, 48)
        self.text_color = (230, 230, 230)
        self.game_active = False
        self.points_player_one = 1
        self.points_player_two = 0
        self.ball = ball
        self.prep_score()



    def prep_score(self):
        score_str = str(self.points_player_one)
        self.score_image_player_one = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        score_str = str(self.points_player_two)
        self.score_image_player_two = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect_right = self.score_image_player_one.get_rect()
        self.score_rect_left = self.score_image_player_two.get_rect()
        self.score_rect_right.right = self.screen_rect.right - 20
        self.score_rect_left.left = self.screen_rect.left + 20
        self.score_rect_right.top = 20
        self.score_rect_left.top = 20
        print(self.points_player_one)
        print(self.points_player_two)



    def update_score(self, ball):
        score_str = str(ball.score_left)
        self.score_image_player_one = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        score_str = str(ball.score_right)
        self.score_image_player_two = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect_right = self.score_image_player_one.get_rect()
        self.score_rect_left = self.score_image_player_two.get_rect()
        self.score_rect_right.right = self.screen_rect.right - 20
        self.score_rect_left.left = self.screen_rect.left + 20
        self.score_rect_right.top = 20
        self.score_rect_left.top = 20




    def show_score(self):
        self.screen.blit(self.score_image_player_one, self.score_rect_right)
        self.screen.blit(self.score_image_player_two, self.score_rect_left)