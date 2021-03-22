

class Settings():
    def __init__(self):
        self.window_height = 570
        self.window_width = 900
        self.bg_color = (0,0,0)
        self.paddle_color = 255,255,255
        self.paddle_position = 400
        self.paddle_speed = 2
#        self.paddle_moving_up = False
#        self.paddle_moving_down = False

        self.paddle_two_color = 255, 255, 255
        self.paddle_two_position = 400
        self.paddle_two_speed = 2
#        self.paddle_two_moving_up = False
#        self.paddle_two_moving_down = False

        self.points_player_one = 0
        self.points_player_two = 0

        #self.game_type =


        #Different parts of the paddle.  Send the ball bouncing at different trajectories.
#       self.top_quarter
#       self.second_quarter
#       self.third_quarter
#       self.bottom_quarter = True