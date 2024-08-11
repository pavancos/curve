import numpy as np
import matplotlib.pyplot as plt
from curve_identification import is_line, is_circle, regularize_line, regularize_circle, detect_symmetry, complete_curve

def process_curve(XYs):
    """Process a curve"""
    if is_line(XYs):
        new_XYs = regularize_line(XYs)
    elif is_circle(XYs):
        new_XYs = regularize_circle(XYs)
    else:
        new_XYs = XYs
    symmetry = detect_symmetry(new_XYs)
    if symmetry:
        print(f"Detected {symmetry} symmetry")
    return new_XYs

def plot_curves(paths_XYs):
    """Plot curves"""
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    colours = ['b', 'g', 'r', 'c','m', 'y', 'k']
    for i, XYs in enumerate(paths_XYs):
        c = colours[i % len(colours)]
        ax.plot(XYs[:, 0], XYs[:, 1], c=c, linewidth=2)
    ax.set_aspect('equal')
    plt.show()

# Example usage
paths_XYs = read_csv('path_to_your_csv.csv')
processed_paths_XYs = [process_curve(XYs) for XYs in paths_XYs]
plot_curves(processed_paths_XYs)