from manim import *

__all__ = [
    "EmitWaveAtPoint",
    "EmitWaves",
]


class EmitWaveAtPoint(Animation):
    CONFIG = {
        "small_radius": 0.0,
        "big_radius": 5,
        "start_stroke_width": 8,
        "color": BLUE,
        "lag_ratio": 0.1,
        "rate_func": linear,
    }

    def __init__(self, source, **kwargs):
        digest_config(self, kwargs)
        self.source = source
        self.mobject = Circle(
            radius=self.big_radius,
            stroke_color=self.color,
            stroke_width=self.start_stroke_width,
        )
        self.mobject.move_to(source)

        def spawn_at_point(mobj, dt):
            mobj.move_to(self.source)
            # self.mobject.clear_updaters()

        self.mobject.add_updater(spawn_at_point)

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.set_width(alpha * self.big_radius)
        self.mobject.set_stroke(width=(1 - alpha) * self.start_stroke_width)


class EmitWaves(LaggedStart):
    CONFIG = {
        "small_radius": 0.0,
        "big_radius": 5,
        "n_circles": 2,
        "start_stroke_width": 8,
        "color": WHITE,
        "remover": True,
        "lag_ratio": 0.6,
        "run_time": 1,
        "remover": True,
    }

    def __init__(self, focal_point, **kwargs):
        digest_config(self, kwargs)
        self.focal_point = focal_point
        animations = [EmitWaveAtPoint(focal_point) for x in range(self.n_circles)]
        super().__init__(*animations, **kwargs)
