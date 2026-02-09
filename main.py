import pandas as pd
import matplotlib.pyplot as plt
import time
import copy
import sys

import Search
import Sorting


# Helper: Plotting
def plot_bar_chart(data, x_idx, y_idx, title, x_label, y_label):
    if not data:
        print("No data to plot.")
        return

    x_values = [str(row[x_idx]) for row in data]
    y_values = [row[y_idx] for row in data]

    plt.figure(figsize=(12, 6))
    # Green for Sorted, Orange for Unsorted/Raw
    bar_color = 'green' if 'Sorted' in title else 'orange'

    plt.bar(x_values, y_values, color=bar_color, edgecolor='black')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Helper: Time Comparison
def compare_sorting_times(full_data, col_idx):
    sizes = [10, 50, 100, len(full_data)]
    sizes = sorted(list(set([s for s in sizes if s <= len(full_data)])))

    times_insertion = []
    times_merge = []
    times_quick = []

    print(f"\n{'Size':<10} | {'Insertion (s)':<15} | {'Merge (s)':<15} | {'Quick (s)':<15}")
    print("-" * 65)

    for n in sizes:
        subset = full_data[:n]

        # 1. Insertion Sort
        data_copy = copy.deepcopy(subset)
        start = time.perf_counter()
        Sorting.insertion_sort(data_copy, col_idx)
        times_insertion.append(time.perf_counter() - start)

        # 2. Merge Sort
        data_copy = copy.deepcopy(subset)
        start = time.perf_counter()
        Sorting.merge_sort(data_copy, col_idx)
        times_merge.append(time.perf_counter() - start)

        # 3. Quick Sort
        data_copy = copy.deepcopy(subset)
        start = time.perf_counter()
        res = Sorting.quick_sort(data_copy, col_idx)
        times_quick.append(time.perf_counter() - start)

        print(f"{n:<10} | {times_insertion[-1]:.6f}          | {times_merge[-1]:.6f}          | {times_quick[-1]:.6f}")

    # Plot Comparison
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_insertion, label='Insertion Sort', marker='o')
    plt.plot(sizes, times_merge, label='Merge Sort', marker='s')
    plt.plot(sizes, times_quick, label='Quick Sort', marker='^')
    plt.xlabel('Input Size (Rows)')
    plt.ylabel('Time (Seconds)')
    plt.title('Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    # 1. Load Data
    try:
        df = pd.read_excel('Covid Dashboard.xlsx', sheet_name='Data')
    except Exception:
        try:
            df = pd.read_csv('Covid Dashboard.xlsx - Data.csv')
        except FileNotFoundError:
            print("Error: Could not find data file.")
            return

    df.fillna(0, inplace=True)
    data = df.values.tolist()
    data_2d_array = df.values.tolist()
    columns = df.columns.tolist()

    # Print fist and last 10 rows
    print("Columns:", columns)
    print("-" * 20)
    print("First 10 Rows of the spreadsheet")

    for i in range(min(10, len(data_2d_array))):
        print("Row ", i, ":", data_2d_array[i])
    print("-" * 20)
    print("Last 10 Rows of the spreadsheet")

    total_rows = len(data_2d_array)
    start_index = max(0, total_rows - 10)

    for i in range(start_index, total_rows):
        print("Row ", i, ":", data_2d_array[i])

    # Define Column Names
    COL_STATE = 'State/UTs'
    COL_CASES = 'Total Cases'
    COL_ZONE = 'Zone'

    try:
        idx_state = columns.index(COL_STATE)
        idx_cases = columns.index(COL_CASES)
        idx_zone = columns.index(COL_ZONE)
    except ValueError as e:
        print(f"Column error: {e}")
        return

    # PART 1: VISUALIZE UNSORTED
    print("\n1. Unsorted Data Visualization")
    plot_bar_chart(data[:10], idx_state, idx_cases,
                   "First 10 States (Unsorted)", COL_STATE, COL_CASES)


    # PART 2: SEARCHING ALGORITHMS
    print("\n2. Searching Scenarios")

    # Scenario A: Search by STATE (Linear)
    print(f"\n[Scenario A] Linear Search in '{COL_STATE}'")

    target_found = "Delhi"
    target_not_found = "Atlantis"

    # 1. Successful Search
    print(f"Searching for '{target_found}'...")
    # Passing: data, column_index, value
    res = Search.linear_search(data, idx_state, target_found)
    if res != -1:
        print(f"Found at row index {res}")
        # Print the data found to prove it
        if isinstance(res, list):
            print(f"Data: {data[res[0]]}")
    else:
        print(f"Failed to find '{target_found}'")

    # 2. Unsuccessful Search
    print(f"Searching for '{target_not_found}'...")
    res = Search.linear_search(data, idx_state, target_not_found)
    if res == -1 or res == []:
        print("SUCCESS: Correctly identified as not found.")
    else:
        print(f"FAILED: Found {res}")

    # Scenario B: Search by ZONE (Linear)
    print(f"\n[Scenario B] Linear Search in '{COL_ZONE}'")
    target_zone = "South"

    print(f"Searching for all rows in '{target_zone}' Zone...")
    res = Search.linear_search(data, idx_zone, target_zone)
    if res != -1 and len(res) > 0:
        print(f"SUCCESS: Found {len(res)} states in {target_zone} Zone.")
    else:
        print("Not Found.")

    # Scenario C: Binary Search (Must Sort First)
    print(f"\n[Scenario C] Binary Search in '{COL_STATE}'")
    print("   (Sorting data by State name first...)")

    # Sort a copy for Binary Search
    sorted_by_name = Sorting.quick_sort(copy.deepcopy(data), idx_state)

    print(f"Binary searching for '{target_found}'...")
    found_row = Search.binary_search(sorted_by_name, idx_state, target_found)

    if found_row:
        print(f"SUCCESS: Found row starting with {found_row[0]}")
    else:
        print("Not Found.")

    # Scenario D: Search by Total Cases (Numeric)
    print(f"\n[Scenario D] Binary Search in '{COL_ZONE}'")
    print("   (Sorting data by State name first...)")

    # Sort a copy for Binary Search
    sorted_by_zone = Sorting.quick_sort(copy.deepcopy(data), idx_zone)

    target_zone = "South"
    print(f"Searching for all rows in '{target_zone}' Zone...")
    found_row = Search.binary_search(sorted_by_zone, idx_zone, target_zone)
    if found_row:
        print(f"SUCCESS: Found a record in '{target_zone}': {found_row[idx_state]}")
    else:
        print("Not found.")

    # PART 3: SORTING & VISUALIZATION
    print("\n3. Sorting & Visualization")
    print(f"Sorting by '{COL_CASES}'...")

    # Sort a fresh copy for the final result
    sorted_data = Sorting.quick_sort(copy.deepcopy(data), idx_cases)

    # Get Top 10 (Highest cases)
    # Assuming Ascending sort -> Last 10 are highest -> Reverse to show top first
    top_10 = sorted_data[-10:]
    top_10.reverse()

    plot_bar_chart(top_10, idx_state, idx_cases,
                   f"Top 10 States by {COL_CASES} (Sorted)", COL_STATE, COL_CASES)

    # PART 4: PERFORMANCE COMPARISON
    print("\n4. Performance Comparison")
    compare_sorting_times(data, idx_cases)


if __name__ == "__main__":
    main()