import time


def insertionsort(arr):
    start_time = time.time()
    # für jedes Element im Array
    for i in range(1, len(arr)):
        key = arr[i]
        # jedes Element, das größer als key ist, eine Position nach vorn schieben
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    duration = (time.time() - start_time) * 1000000
    # return arr, duration
    return round(duration, 2)
