def binary_search(arr, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2

    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return arr[mid]


if __name__ == "__main__":
    print(binary_search((1, 3, 5, 7, 9, 11, 13, 15, 17, 19), 7, 0, 9))
