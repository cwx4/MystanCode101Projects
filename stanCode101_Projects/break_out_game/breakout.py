"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():

    graphics = BreakoutGraphics()

    # Add animation loop here!
    dx = graphics.ball_move_x()
    dy = graphics.ball_move_y()
    lives = NUM_LIVES
    while True:
        if graphics.ball_out():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                break
        graphics.move_ball()
        graphics.check_for_collisions()
        graphics.handle_wall_condition()
        # graphics.check_for_collisions()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
