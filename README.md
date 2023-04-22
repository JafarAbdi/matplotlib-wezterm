# matplotlib-wezterm

[![Format](https://github.com/JafarAbdi/matplotlib-wezterm/actions/workflows/format.yml/badge.svg)](https://github.com/JafarAbdi/matplotlib-wezterm/actions/workflows/format.yml)

A matplotlib backend for [wezterm](https://github.com/wez/wezterm/).
The code is based on [itermplot](https://github.com/daleroberts/itermplot)

## Installation

Assuming you have [micromamba](https://mamba.readthedocs.io/en/latest/installation.html#automatic-installation)

```bash
micromamba create -f environment.yml
micromamba run -n matplotlib-wezterm pip install .
```

## Usage

```bash
MPLBACKEND='module://matplotlib_wezterm' micromamba run -n matplotlib-wezterm ipython
```

[![demo-manual]](https://user-images.githubusercontent.com/16278108/233807919-eef927ea-ae60-424c-abe2-63435849be5f.mp4)

If you want to show the plot without explicitly calling `plt.show()`
create the following `~/.ipython/profile_default/startup/wezterm.py`
with the following content:

```python
import os


def enable_wezterm():
    import matplotlib.pyplot as plt
    import matplotlib

    def display_and_reset(*args):
        plt.show()
        plt.figure()  # New figure for next plot (don't re-use)

    # Tell IPython to display matplotlib figures automatically
    from IPython import get_ipython

    formatter = get_ipython().display_formatter.formatters["text/plain"]
    formatter.for_type(matplotlib.artist.Artist, display_and_reset)
    formatter.for_type(matplotlib.axes.Axes, display_and_reset)



if os.environ.get("MPLBACKEND", "") == "module://matplotlib_wezterm":
    enable_wezterm()
```

[![demo-auto]](https://user-images.githubusercontent.com/16278108/233807925-1d2c92ed-fa16-43e8-a609-3aa07e39e36c.mp4)
