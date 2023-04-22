"""A matplotlib backend for wezterm."""

import io
from subprocess import run

import matplotlib
from matplotlib._pylab_helpers import Gcf
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


def draw_if_interactive():
    if matplotlib.is_interactive():
        figure_manager = Gcf.get_active()
        if figure_manager is not None:
            figure_manager.show()


def show():
    figure_manager = Gcf.get_active()
    if figure_manager is not None:
        figure_manager.show()
    else:
        for manager in Gcf.get_all_fig_managers():
            manager.show()


def new_figure_manager(num, *args, **kwargs):
    FigureClass = kwargs.pop("FigureClass", Figure)  # noqa: N806
    this_figure = FigureClass(*args, **kwargs)
    return new_figure_manager_given_figure(num, this_figure)


def new_figure_manager_given_figure(num, figure):
    canvas = FigureCanvas(figure)
    return FigureManager(canvas, num)


class WeztermFigureManager(FigureManagerBase):
    def __init__(self, canvas, num) -> None:
        FigureManagerBase.__init__(self, canvas, num)

    def show(self):
        data = io.BytesIO()

        self.canvas.print_figure(data, dpi=200)

        run(
            ["wezterm", "imgcat"],
            capture_output=False,
            text=False,
            input=data.getbuffer(),
        )


FigureCanvas = FigureCanvasAgg
FigureManager = WeztermFigureManager
