"""
File: my_drawing.py
Name: Sylvia Chang
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc,GLabel,GCompound,G3DRect,GLine,GObject,GFillableObject
from campy.graphics.gwindow import GWindow

import random as r
SIZE = 30
START_POINT = 0
window = GWindow(width=500, height=500, title='No Title')
END_POINT = window.height-SIZE


def main():
    """
    This is a drawing with no title because drawing is too hard for me.
    """
    triangle = GPolygon()
    triangle.add_vertex((0+SIZE, -20+SIZE))
    triangle.add_vertex((-15+SIZE, 10+SIZE))
    triangle.add_vertex((15+SIZE, 10+SIZE))
    window.add(triangle,r.randrange(START_POINT, END_POINT),r.randrange(START_POINT, END_POINT))
    triangle.filled = True
    triangle.fill_color = 'red'

    triangle = GPolygon()
    triangle.add_vertex((0+SIZE, -20+SIZE))
    triangle.add_vertex((-15+SIZE, 10+SIZE))
    triangle.add_vertex((15+SIZE, 10+SIZE))
    window.add(triangle,r.randrange(START_POINT, END_POINT),r.randrange(START_POINT, END_POINT))
    triangle.filled = True
    triangle.fill_color = 'red'

    rect = GRect(SIZE, SIZE)
    window.add(rect, r.randrange(START_POINT, END_POINT), r.randrange(START_POINT, END_POINT))
    rect.filled = True
    rect.fill_color = 'yellow'

    rect = GRect(SIZE, SIZE)
    window.add(rect, r.randrange(START_POINT, END_POINT), r.randrange(START_POINT, END_POINT))
    rect.fill_color = 'yellow'

    ball = GOval(SIZE, SIZE)
    window.add(ball, r.randrange(START_POINT, END_POINT), r.randrange(START_POINT, END_POINT))
    ball.filled = True
    ball.fill_color = 'green'

    ball = GOval(SIZE, SIZE)
    window.add(ball, r.randrange(START_POINT, END_POINT), r.randrange(START_POINT, END_POINT))
    ball.fill_color = 'green'

    wig_upper = GArc(150, 250 ,0, 180, x=200 ,y=100)
    wig_upper.filled = True
    wig_upper.fill_color = 'gold'
    wig_upper.color = 'gold'
    window.add(wig_upper)

    body = GOval(80, 220)
    body.filled = True
    body.fill_color = 'royalblue'
    body.color = 'royalblue'
    window.add(body, x=237, y=210)

    face = GArc(100, 225, 0, -180, x=225, y=108)
    face.filled = True
    face.fill_color = 'lightcyan'
    face.color = 'lightcyan'
    window.add(face)

    mouth = GArc(30,25,0,-160, x=265,y=200)
    mouth.filled = True
    mouth.fill_color= 'red'
    mouth.color = 'red'
    window.add(mouth)

    line = GLabel('DON\'T LEAVE ')
    line.font = 'Courier-20'
    window.add(line, line.width, r.randrange(START_POINT, END_POINT))
    line.color ='dodgerblue'

    glass = GPolygon()
    glass.add_vertex((-5,0))
    glass.add_vertex((0,-10))
    glass.add_vertex((5,0))
    glass.add_vertex((0,10))
    window.add(glass,x=250,y=180)
    glass.filled =True
    glass.fill_color ='black'

    glass = GPolygon()
    glass.add_vertex((-5,0))
    glass.add_vertex((0,-10))
    glass.add_vertex((5,0))
    glass.add_vertex((0,10))
    window.add(glass,x=300,y=180)
    glass.filled =True
    glass.fill_color ='black'

    line = GLine(100,0,100,180)
    window.add(line)

    mic = GPolygon()
    mic.add_vertex((-10, -20))
    mic.add_vertex((10, -20))
    mic.add_vertex((-10, 20))
    mic.add_vertex((10, 20))
    window.add(mic, x=100, y=180)
    mic.filled = True
    mic.fill_color = 'black'


if __name__ == '__main__':
    main()
