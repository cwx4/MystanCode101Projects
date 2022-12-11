"""
File: bouncing_ball.py
Name: Sylvia Chang
-------------------------
This program plays a game called
"bouncing ball" in which players click
the mouse and the ball will bounce
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# global variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'red'
    ball.color = 'red'
    window.add(ball, START_X, START_Y)
    onmouseclicked(stimulate)


def stimulate(mouse):
    """
    Clicking the mouse will stimulate the fall_down function
    """
    global count
    count += 1
    if count <= 3:
        any_point = window.get_object_at(mouse.x, mouse.y)
        if any_point is None or any_point is not None:
            fall_down()


def fall_down():
    """
    The program show the animation of bouncing ball
    """
    vx = VX
    vy = 0
    y = START_Y
    while True:
        onmouseclicked(no_react)
        ball.move(vx, vy)
        if ball.y >= window.height-SIZE:
            # ball hit the floor
            vy = -vy
            y *= REDUCE
        if vy >= 0:
            # ball fall
            vy += GRAVITY
        else:
            # ball bounce
            if ball.y >= y:
                vy += GRAVITY
            else:
                # bounce to the limit and begin to fall
                vy = -vy
        if ball.x > window.width:
            break
        pause(DELAY)
    window.add(ball, START_X, START_Y)
    onmouseclicked(stimulate)


def no_react(click):
    """
    When the ball is bouncing, clicking the mouse has no reaction
    """
    any_point = window.get_object_at(click.x, click.y)
    if any_point is None or any_point is not None:
        pass


if __name__ == "__main__":
    main()
