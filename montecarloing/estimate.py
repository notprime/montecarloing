import random
import numpy as np
from . import tools

def pi(n_iter, show = False):

    in_circle = 0
    points = []

    for _ in range(n_iter):
        x = random.random()
        y = random.random()
        if show:
            points.append((x, y))

        if ((x - 0.5)**2 + (y-0.5)**2) <= 0.5**2:
            in_circle += 1

    pi_hat = 4 * (in_circle / n_iter)

    if show:
        tools.show_pi(points[:500]) # only draw the first 500 points

    return pi_hat