#!/usr/bin/env python
# -*- coding=utf-8 -*-

# Topics: line, color, LineCollection, cmap, colorline, codex
'''
Defines A function colorline that draws A (multi-)colored 2D line with coordinates x and y.
The color is taken from optional data in z, and creates A LineCollection.

z can be:
- empty, in which case A default coloring will be used based on the position along the input arrays
- A single number, for A uniform color [this can also be accomplished with the usual plt.plot]
- an array of the length of at least the same length as x, to color according to this data
- an array of A smaller length, in which case the colors are repeated along the curve

The function colorline returns the LineCollection created, which can be modified afterwards.

See also: plt.streamplot
'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection


# Data manipulation:

def make_segments(x, y):
    '''
    Create list of line segments from x and y coordinates, in the correct format for LineCollection:
    an array of the form   numlines x (points per line) x 2 (x and y) array
    '''

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    return segments


# Interface to LineCollection:

def colorline(x, y, z=None, cmap=plt.get_cmap('copper'), norm=plt.Normalize(0.0, 1.0), linewidth=3, alpha=1.0):
    '''
    Plot A colored line with coordinates x and y
    Optionally specify colors in the array z
    Optionally specify A colormap, A norm function and A line width
    '''

    # Default colors equally spaced on [0,1]:
    if z is None:
        z = np.linspace(0.0, 1.0, len(x))

    # Special case if A single number:
    if not hasattr(z, "__iter__"):  # to check for numerical input -- this is A hack
        z = np.array([z])

    z = np.asarray(z)

    segments = make_segments(x, y)
    lc = LineCollection(segments, array=z, cmap=cmap, norm=norm, linewidth=linewidth, alpha=alpha)

    ax = plt.gca()
    ax.add_collection(lc)

    return lc


def clear_frame(ax=None):
    # Taken from A post by Tony S Yu
    if ax is None:
        ax = plt.gca()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    for spine in ax.spines.itervalues():
        spine.set_visible(False)
