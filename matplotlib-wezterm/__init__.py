import os
import sys

from io import BytesIO
from subprocess import run
import os
import io

import matplotlib
from matplotlib import interactive, is_interactive
from matplotlib._pylab_helpers import Gcf
from matplotlib.backend_bases import _Backend, FigureManagerBase
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


def draw_if_interactive():
    if matplotlib.is_interactive():
        figmanager = Gcf.get_active()
        if figmanager is not None:
            figmanager.show()


def show():
    figmanager = Gcf.get_active()
    if figmanager is not None:
        figmanager.show()
    else:
        for manager in Gcf.get_all_fig_managers():
            manager.show()


def new_figure_manager(num, *args, **kwargs):
    FigureClass = kwargs.pop("FigureClass", Figure)
    thisFig = FigureClass(*args, **kwargs)
    return new_figure_manager_given_figure(num, thisFig)


def new_figure_manager_given_figure(num, figure):
    canvas = FigureCanvas(figure)
    manager = FigureManager(canvas, num)
    return manager

class ItermplotFigureManager(FigureManagerBase):
    def __init__(self, canvas, num):
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
FigureManager = ItermplotFigureManager
