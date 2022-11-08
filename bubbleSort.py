import time


def bubblesort(arr):
    start_time = time.time()
    n = len(arr)
    # für jedes Element im Array
    for i in range(n - 1):
        # nacheinander schauen
        for j in range(0, n - i - 1):
            # ob Element getauscht werden soll, wenn j > j+1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    duration = (time.time() - start_time) * 1000000
    # return arr, duration
    return round(duration, 2)
