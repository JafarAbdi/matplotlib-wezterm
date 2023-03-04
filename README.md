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
MPLBACKEND='module://matplotlib-wezterm' micromamba run -n matplotlib-wezterm ipython
```
