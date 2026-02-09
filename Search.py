import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('Covid Dashboard.xlsx', sheet_name='Data')
data_2d_array = df.values.tolist()

columns = df.columns.tolist()

def linear_search(array, search_column, search_value ):
    col_index = -1
    for i in range(len(columns)):
        if columns[i] == search_column:
            col_index = i
            break

    if col_index == -1:
        return [-1]

    matches = []
    for i in range(len(array)):
        row = array[i]
        if i < len(array) and col_index < len(row):
            cell_value = row[col_index]

            if cell_value is None or (isinstance(cell_value, float) and np.isnan(cell_value)):
                continue

            if str(cell_value) == str(search_value):
                matches.append(i)

    if matches:
        return matches
    else:
        return -1

def binary_search(arr, col_idx, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid][col_idx] == target:
            return arr[mid]
        elif arr[mid][col_idx] > target:
            high = mid - 1
        else:
            low = mid + 1

    return None