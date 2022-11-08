from bubbleSort import *
from insertionSort import *
from selectionSort import *
from numpySort import *
import numpy as np
import csv


def collect_durations(loops):
    row = [0.0, 0.0, 0.0, 0.0]
    result = np.array([0.0, 0.0, 0.0, 0.0])
    for n in range(0, loops + 1):
        arr0 = np.random.randint(0, 200, 10)
        arr1 = arr0
        arr2 = arr0
        arr3 = arr0
        arr4 = arr0
        row[0] = bubblesort(arr1)
        row[1] = insertionsort(arr2)
        row[2] = selectionsort(arr3)
        row[3] = numpysort(arr4)
        result = np.vstack((result, row))
    result = np.delete(result, (0, 1), 0)
    return result


def write_csv(rows):
    fields = ['Bubblesort', 'Insertionsort', 'Selectionsort', 'Numpysort']
    filename = "sort_algorithm_comparison.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def calculations(array):
    mean = np.mean(array, 0)
    std = np.std(array, 0)
    meanstdperc0 = str(round(mean[0], 2)) + " µs ± " + str(round(std[0], 2)) + " µs CV: " + str(
        round(std[0] / mean[0] * 100, 2)) + " %"
    meanstdperc1 = str(round(mean[1], 2)) + " µs ± " + str(round(std[1], 2)) + " µs CV:" + str(
        round(std[1] / mean[1] * 100, 2)) + " %"
    meanstdperc2 = str(round(mean[2], 2)) + " µs ± " + str(round(std[2], 2)) + " µs CV:" + str(
        round(std[2] / mean[2] * 100, 2)) + " %"
    meanstdperc3 = str(round(mean[3], 2)) + " µs ± " + str(round(std[3], 2)) + " µs CV:" + str(
        round(std[3] / mean[3] * 100, 2)) + " %"
    print("Bubblesort:    " + meanstdperc0)
    print("Insertionsort: " + meanstdperc1)
    print("Selectionsort: " + meanstdperc2)
    print("Numpysort:     " + meanstdperc3)


if __name__ == '__main__':
    # write_csv(collect_durations(30))
    calculations(collect_durations(10))
