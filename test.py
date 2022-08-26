def binarySearch(arr, low, high, key):
    if low > high:
        return -1
    mid = low + (high - low)/2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, low, mid-1, key)
    else:
        return binarySearch(arr, mid+1, high, key)
