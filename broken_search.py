# ID 85064124
def broken_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        array_mid = array[mid]
        array_left = array[left]
        array_right = array[right]
        if array_mid == target:
            return mid
        elif array_left == target:
            return left
        elif array_right == target:
            return right
        elif array_left <= array_mid:
            if array_left < target < array_mid:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if array_mid < target < array_right:
                left = mid + 1
            else:
                right = mid - 1
    return -1
