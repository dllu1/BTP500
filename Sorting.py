import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Covid Dashboard.xlsx', sheet_name='Data')
data_2d_array = df.values.tolist()

columns = df.columns.tolist()

def bar_plot(array):



def insertion_sort(arr, col_idx):
    left = 0
    right = None

    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        curr = arr[i]
        j = i

        while j > left and arr[j - 1][col_idx] > curr[col_idx]:
            arr[j] = arr[j - 1]
            j = j - 1

        arr[j] = curr

def merge_sort(arr, col_idx):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    merge_sort(left, col_idx)
    merge_sort(right, col_idx)

    i = j = k = 0
    while i < len(left) and j < len(right):
        """Compare based on the chosen column index"""
        if left[i][col_idx] < right[j][col_idx]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def quick_sort(arr, col_idx):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[col_idx] < pivot[col_idx]]
    right = [x for x in arr if x[col_idx] > pivot[col_idx]]
    middle = [x for x in arr if x[col_idx] == pivot[col_idx]]

    return quick_sort(left, col_idx) + middle + quick_sort(right, col_idx)