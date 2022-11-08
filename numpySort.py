import time
import numpy as np


def numpysort(arr):
    start_time = time.time()
    np.sort(arr)
    duration = (time.time() - start_time) * 1000000
    return round(duration, 2)
