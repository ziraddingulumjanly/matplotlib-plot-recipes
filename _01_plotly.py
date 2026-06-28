"""Matplotlib Plot Recipes

Line-based plotting patterns for mathematical functions.
"""

import numpy as np
import matplotlib.pyplot as plt


"""Shared visual style."""

plt.rcParams["figure.dpi"] = 600
plt.rcParams["savefig.dpi"] = 600
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"

niceblue = "#4d7da7"
nicered = "#e15656"
nicegreen = "#6dc350"
nicegray = "#6e6e6e"
nicemagenta = "#c55aaa"


"""Five functions on one line plot with explicit line-width settings."""

x = np.linspace(-2.5, 2.5, 1000)

y1 = np.exp(0.5 * x - 1) * (x + 1) ** 2
y2 = np.sin(x) * np.cos(x)
y3 = np.tanh(x)
y4 = x**2 - 2
y5 = np.cos(2 * x)

plt.figure(figsize=(8, 5))

plt.plot(x, y1, color=niceblue, linewidth=2.5, label=r"$e^{0.5x-1}(x+1)^2$")
plt.plot(x, y2, color=nicered, linewidth=2.5, label=r"$\sin(x)\cos(x)$")
plt.plot(x, y3, color=nicegreen, linewidth=2.5, label=r"$\tanh(x)$")
plt.plot(x, y4, color=nicegray, linewidth=2.5, label=r"$x^2 - 2$")
plt.plot(x, y5, color=nicemagenta, linewidth=2.5, label=r"$\cos(2x)$")

plt.title(r"Comparison of Five Mathematical Functions", fontsize=14, pad=12)
plt.xlabel(r"$x$", fontsize=12)
plt.ylabel(r"$f(x)$", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(
    loc="upper left",
    frameon=True,
    facecolor="w",
    edgecolor="#e0e0e0",
    fontsize=10,
)

plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 3.5)
plt.tight_layout()

plt.show()


"""Five functions with centralized typography and line-width settings."""

base_fontsize = 18
linewidth = 1.5

plt.rcParams["lines.linewidth"] = linewidth
plt.rcParams["axes.labelsize"] = base_fontsize
plt.rcParams["axes.titlesize"] = base_fontsize
plt.rcParams["xtick.labelsize"] = base_fontsize - 3
plt.rcParams["ytick.labelsize"] = base_fontsize - 3
plt.rcParams["legend.fontsize"] = base_fontsize - 4

x = np.linspace(-2.5, 2.5, 1000)

y1 = np.exp(0.5 * x - 1) * (x + 1) ** 2
y2 = np.sin(x) * np.cos(x)
y3 = np.tanh(x)
y4 = x**2 - 2
y5 = np.cos(2 * x)

plt.figure(figsize=(9, 6))

plt.plot(x, y1, color=niceblue, label=r"$e^{0.5x-1}(x+1)^2$")
plt.plot(x, y2, color=nicered, label=r"$\sin(x)\cos(x)$")
plt.plot(x, y3, color=nicegreen, label=r"$\tanh(x)$")
plt.plot(x, y4, color=nicegray, label=r"$x^2 - 2$")
plt.plot(x, y5, color=nicemagenta, label=r"$\cos(2x)$")

plt.title(r"Comparison of Five Mathematical Functions", pad=15)
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper left", frameon=True, facecolor="w", edgecolor="#e0e0e0")

plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 3.5)
plt.tight_layout()

plt.show()


"""Four separate line panels."""

x = np.linspace(-3, 3, 1000)

y1 = np.exp(0.5 * x - 1) * (x + 1) ** 2
y2 = np.sin(x) * np.cos(x)
y3 = np.tanh(x)
y4 = x**2 - 2

fig, axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True)

axes[0, 0].plot(x, y1, color=niceblue)
axes[0, 0].set_title(r"$e^{0.5x-1}(x+1)^2$")
axes[0, 0].set_ylabel(r"$f(x)$")

axes[0, 1].plot(x, y2, color=nicered)
axes[0, 1].set_title(r"$\sin(x)\cos(x)$")

axes[1, 0].plot(x, y3, color=nicegreen)
axes[1, 0].set_title(r"$\tanh(x)$")
axes[1, 0].set_xlabel(r"$x$")
axes[1, 0].set_ylabel(r"$f(x)$")

axes[1, 1].plot(x, y4, color=nicegray)
axes[1, 1].set_title(r"$x^2 - 2$")
axes[1, 1].set_xlabel(r"$x$")

for axis in axes.ravel():
    axis.grid(True, linestyle="--", alpha=0.5)

fig.suptitle("Functions in Separate Panels", y=1.02)
fig.tight_layout()

plt.show()


"""To save a figure, place one of these lines before plt.show()."""

"""
plt.savefig("my_line_plot.png", dpi=600, bbox_inches="tight")
plt.savefig("my_line_plot.pdf", bbox_inches="tight")
"""
