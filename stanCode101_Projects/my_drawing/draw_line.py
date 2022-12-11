"""
File: draw_line.py
Name: Sylvia Chang
-------------------------
User can draw a line with clicks on the window
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 30
window = GWindow()
circle = GOval(SIZE, SIZE)
point_x = None
point_y = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    circle.filled = True
    circle.fill_color = 'crimson'
    circle.color = 'teal'
    onmouseclicked(point)


def point(mouse):
    """
    Ths first time click show the circle and locate one side of line
    """
    window.add(circle, mouse.x-SIZE/2, mouse.y-SIZE/2)
    global point_x
    global point_y
    point_x = mouse.x
    point_y = mouse.y
    if point_x is not None and point_y is not None:
        onmouseclicked(point_2)


def point_2(click):
    """
    The second click show the line, remove the circle, reset point_x and point_y
    """
    global point_x
    global point_y
    line = GLine(point_x, point_y, click.x, click.y)
    window.add(line)
    point_x = None
    point_y = None
    window.remove(circle)
    onmouseclicked(point)





if __name__ == "__main__":
    main()
