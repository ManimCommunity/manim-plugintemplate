from manim import *


class MyDotGrid(VMobject):
    def __init__(self):
        super().__init__(self)
        dot1 = Dot(fill_color=GREEN).shift(LEFT)
        dot2 = Dot(fill_color=BLUE)
        dot3 = Dot(fill_color=RED).shift(RIGHT)
        self.dotgrid = VGroup(dot1, dot2, dot3)
        self.add(self.dotgrid)

    def update_dot(self):
        self.dotgrid.become(self.dotgrid.shift(UP))
