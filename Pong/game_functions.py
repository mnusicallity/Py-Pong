import pygame
import sys
from paddle import Paddle


def update_screen(play_button, game_menu, stats):
    if not stats.game_active:
        play_button.draw_button()
        game_menu.game_menu()
        game_menu.nav()



def check_events(stats, ball, paddle, paddle_two, play_button, game_menu):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keydown_events(event, stats, ball, paddle, paddle_two, game_menu)


        elif event.type == pygame.KEYUP:
            keyup_events(event, game_menu, paddle, paddle_two)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
            select_menu_option(game_menu, mouse_x, mouse_y)




def check_play_button(stats, play_button, mouse_x, mouse_y):
    """Start a new game when the player clicks Play"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True


def select_menu_option(game_menu, mouse_x, mouse_y):
    if game_menu.right_arrow_rect.collidepoint(mouse_x, mouse_y):
        game_menu.selection += 1
        if game_menu.selection == 3:
            game_menu.selection = 0

    elif game_menu.left_arrow_rect.collidepoint(mouse_x, mouse_y):
        game_menu.selection -= 1
        if game_menu.selection == -1:
            game_menu.selection = 2

    elif game_menu.rect.collidepoint(mouse_x, mouse_y) and game_menu.selection == 2:
        game_menu.select_difficulty = True

    elif game_menu.difficulty_settings_rect.collidepoint(mouse_x, mouse_y):
        game_menu.select_difficulty = False


def keydown_events(event, stats, ball, paddle, paddle_two, game_menu):

    #Press Q to exit

    if event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_RETURN:
        game_menu.select_difficulty = True
        #Create condition for selectiong diffuctuly
        """Branch for changing difficulty being true"""


    elif event.key == pygame.K_RIGHT:
        #if not game_menu.select_difficulty:
        game_menu.selection += 1
        if game_menu.selection == 3:
            game_menu.selection = 0
        #elif game_menu.select_difficulty:
            #game_menu.selection += 1

        print(game_menu.menu_selection[game_menu.selection])

    elif event.key == pygame.K_LEFT:
        game_menu.selection -= 1
        if game_menu.selection == -1:
            game_menu.selection = 2
        #print(game_menu.menu_selection[game_menu.selection])

    elif event.key == pygame.K_DOWN:
        paddle.paddle_moving_down = True
    elif event.key == pygame.K_UP:
        paddle.paddle_moving_up = True

    elif event.key == pygame.K_s:
        paddle_two.paddle_moving_down = True
    elif event.key == pygame.K_w:
        paddle_two.paddle_moving_up = True

    #Makes X in upper right quit when pressed
    elif event.type == pygame.QUIT:
        sys.exit()

def keyup_events(event, game_menu, paddle, paddle_two):

    if event.key == pygame.K_DOWN:
        paddle.paddle_moving_down = False

    elif event.key == pygame.K_UP:
        paddle.paddle_moving_up = False

    if event.key == pygame.K_s:
        paddle_two.paddle_moving_down = False

    elif event.key == pygame.K_w:
        paddle_two.paddle_moving_up = False


def create_player_one_paddle():
    play_one_paddle = Paddle()