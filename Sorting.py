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