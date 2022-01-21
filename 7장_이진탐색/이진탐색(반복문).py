def binary_search(arr, target, start, end):
    while start <= end:
        mid = start + end // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return arr[mid]
    return


if __name__ == "__main__":
    print(binary_search((1, 3, 5, 7, 9, 11, 13, 15, 17, 19), 7, 0, 9))
