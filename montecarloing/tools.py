import numpy as np
import matplotlib.pyplot as plt


def show_pi(points):

    fig, ax = plt.subplots(figsize = (5, 5))

    # Draw the Circle and the Square
    circle = plt.Circle((0.5, 0.5), 0.5, color = 'blue', alpha = 0.4)
    ax.add_patch(circle)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)# change all spines
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(3)

    # Plot the points
    x_points, y_points = zip(*points)
    ax.scatter(x_points, y_points, color = 'red', alpha = 0.7)

    plt.show()