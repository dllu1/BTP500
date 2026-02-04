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