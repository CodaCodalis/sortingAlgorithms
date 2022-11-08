import time


def selectionsort(arr):
    start_time = time.time()
    # für jedes Element im Array
    for i in range(len(arr)):
        # das kleinste Element finden
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # und das kleinste Element gegen das erste Element tauschen
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    duration = (time.time() - start_time) * 1000000
    # return arr, duration
    return round(duration, 2)
