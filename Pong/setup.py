import pygame
import sys
from settings import Settings
from paddle import Paddle
import game_functions as gf
from ball import Ball
from divider import Divider
from stats import GameStats
from button import Button
from game_menu import GameMenu

pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.window_width, ai_settings.window_height ))
divider = Divider(screen, ai_settings)
paddle = Paddle(screen, ai_settings, 0)
paddle_two = Paddle(screen, ai_settings, 890)
ball = Ball(screen, ai_settings, paddle, paddle_two)
play_button = Button(ai_settings, screen, "Play")
stats = GameStats(ai_settings, screen, ball)
game_menu = GameMenu(screen, ai_settings)
game_menu.dropdown_menu_for_difficulty_settings()

while True:

    #Makes background chosen color and refreshes screen
    gf.update_screen(play_button, game_menu, stats)
    pygame.display.flip()
    screen.fill(ai_settings.bg_color)
    gf.check_events(stats, ball, paddle, paddle_two, play_button, game_menu)
    if stats.game_active:
        stats.update_score(ball)
        stats.show_score()
        paddle_two.update()
        paddle_two.draw_paddle()
        paddle.update()
        paddle.draw_paddle()
        divider.draw()
        ball.move()
        ball.bounce()
        paddle_two.against_ai(ball)
        ball.reset()
        if ball.score_left >= 10 or ball.score_right >= 10:
            stats.game_active = False
            ball.score_left = 0
            ball.score_right = 0
    elif game_menu.select_difficulty:
        game_menu.dropdown_menu_for_difficulty_settings()
    #;o9p'[]-' \
#    '=\poi9'