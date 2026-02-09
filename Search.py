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

# Deaths column Linear Search (Successful)
print("Death Column Linear Search: (Successful)")
deaths_search_result = linear_search(data_2d_array, "Deaths", 5138)
print("Searching for Deaths = 5138:")
print("Result: " + str(deaths_search_result))

if deaths_search_result != -1 and deaths_search_result != [-1]:
    print("Matching rows (first 5 shown):")
    for i, row_idx in enumerate(deaths_search_result[:5]):
        print("Row " + str(row_idx) + ": " + str(data_2d_array[row_idx]))
else:
    print("No matches found or column doesn't exist")

print()

# Population column Linear Search (Successful)
print("Population Column Linear Search: (Successful)")
population_search_result = linear_search(data_2d_array, "Population", 1158040)
print("Searching for Population = 1158040:")
print("Result: " + str(population_search_result))

if population_search_result != -1 and population_search_result != [-1]:
    print("Found " + str(len(population_search_result)) + " matches")
    print("First matching row:")
    print(data_2d_array[population_search_result[0]])
else:
    print("No matches found or column doesn't exist")

print()

# Test 4: Linear Search on non-existent column (Unsuccessful)
print("Unsuccessful Linear Search:")
non_existent_search_result = linear_search(data_2d_array, "ABCDE", 100000)
print("Searching in 'ABCDE' = 100000:")
print("Result: " + str(non_existent_search_result))