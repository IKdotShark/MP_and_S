import numpy as np


def generate_exponential(inv_rate):
    uniform_sample = np.random.rand()
    return inv_rate * np.log(1 - uniform_sample)
