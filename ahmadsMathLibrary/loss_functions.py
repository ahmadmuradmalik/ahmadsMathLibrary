
import numpy as np
import math


def mean_squared_error(y, y_hat):
    res = sum((yi - y_hati)**2 for yi, y_hati in zip(y, y_hat))
    return res/len(y)

def mean_absolute_error(y, y_hat):
    res = sum(math.abs(yi - y_hati) for yi, y_hati in zip(y, y_hat))
    return res/len(y)

def mse(*args):
    return mean_squared_error(*args)

def mae(*args):
    return mean_absolute_error(*args)

def L2(*args):
    return mean_squared_error(*args)

def L1(*args):
    return mean_absolute_error(*args)

def KL_divergence():
    """
    measures the "distance" between two distributions,
    this implements the closed form solution for the case 
    of 2 normal distrubtions.
    """

    return None