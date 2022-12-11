"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GCompound
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.x = (window_width-paddle_width)/2
        self.paddle.y = window_height-paddle_offset
        self.window.add(self.paddle, self.paddle.x, self.paddle.y)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0

        # Initialize our mouse listeners
        onmouseclicked(self.game_start)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(brick_rows):
            color = ['red', 'orange', 'yellow', 'green', 'blue']
            for j in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = color[i//2 % 5]
                brick_x = (brick_width + brick_spacing) * j
                brick_y = brick_offset + (brick_height+brick_spacing) * i
                self.window.add(self.bricks, brick_x, brick_y)

    def paddle_move(self, mouse):
        x = mouse.x - self.paddle.width/2
        if mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = x

    def game_start(self, event):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
            # self.move_ball()
        onmouseclicked(self.no_react)

    def no_react(self, click):
        any_point = self.window.get_object_at(click.x, click.y)
        if any_point is True:
            pass

    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)

    def handle_wall_condition(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        # if self.ball.y <= 0 or self.ball.y + self.ball.height > self.window.height:
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        if self.ball_out():
            self.window.add(self.ball)

    def check_for_collisions(self):
        obj_x = self.ball.x
        obj_y = self.ball.y
        for i in range(0, self.ball.width, self.ball.width):
            for j in range(0, self.ball.width, self.ball.width):
                obj_x += i
                obj_y += j
                obj = self.window.get_object_at(obj_x, obj_y)
                if obj is not None:
                    # if obj is self.bricks:  # don't work
                    if obj is not self.paddle:
                        self.window.remove(obj)
                    self.__dy = -self.__dy
                    # self.__dy = -abs(self.__dy)
                    return

    def ball_out(self):
        outside = self.window.height
        ball_outside = self.ball.y > outside
        return ball_outside

    def reset_ball(self):
        self.ball.x = self.window.width/2
        self.ball.y = self.window.height/2
        self.__dy = 0
        self.__dx = 0

        self.window.add(self.ball)
        onmouseclicked(self.game_start)


    # Getter
    def ball_move_x(self):
        return self.__dx

    def ball_move_y(self):
        return self.__dy
