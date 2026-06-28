# Matplotlib Plot Recipes

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Visualization](https://img.shields.io/badge/Focus-Data%20Visualization-4d7da7?style=for-the-badge)

A focused Matplotlib learning project for creating clean, publication-style mathematical and data visualizations in Python.

The notebook uses a consistent visual system:

- High-resolution output at 600 DPI
- Serif text with Computer Modern math fonts
- Mathematical axis labels and legends with LaTeX notation
- Clear layouts for single figures and multi-panel plots

## What this project covers

- Bar charts with labels, gridlines, and legends
- Plotting several mathematical functions on one figure
- Centralizing font sizes and line widths with `plt.rcParams`
- Custom colors for different lines
- Mathematical titles, axes, and legends with raw LaTeX strings
- A 2 × 2 subplot grid
- Saving figures as high-quality PNG and vector PDF files

## Main visual configuration

```python
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 600
plt.rcParams["savefig.dpi"] = 600
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"

niceblue = "#4d7da7"
nicered = "#e15656"
nicegreen = "#6dc350"
nicegray = "#6e6e6e"
nicemagenta = "#c55aaa"
```

## Example concepts

The notebook compares several functions in one plot:

```python
plt.plot(x, y1, color=niceblue, label=r"$e^{0.5x-1}(x+1)^2$")
plt.plot(x, y2, color=nicered, label=r"$\sin(x)\cos(x)$")
plt.plot(x, y3, color=nicegreen, label=r"$\tanh(x)$")
```

It also demonstrates how to place each function in its own panel using:

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True)
```

## Saving figures

Use PNG for high-resolution images and PDF for vector-quality graphics:

```python
plt.savefig("my_plot.png", dpi=600, bbox_inches="tight")
plt.savefig("my_plot.pdf", bbox_inches="tight")
```

## Intended use

You are welcome to use, adapt, and learn from this project. Attribution is appreciated when you share or build upon the work.