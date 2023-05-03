def merge(array, lf, mid, rg):
    left = array[lf:mid]
    right = array[mid:rg]
    k = lf
    i = 0
    j = 0
    while (lf + i < mid and mid + j < rg):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if lf + i < mid:
        while k < rg:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < rg:
            array[k] = right[j]
            j = j + 1
            k = k + 1
    return array


def merge_sort(array, lf, rg):
    if rg - lf > 1:
        mid = (lf + rg)//2
        merge_sort(array, lf, mid)
        merge_sort(array, mid, rg)
        merge(array, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
