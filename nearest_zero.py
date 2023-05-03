# ID 83820845
def find_distance_to_nearest_zero(array):
    zeros_idx = [index for index, value in enumerate(array) if value == 0]
    result = [0] * len(array)
    for index in range(zeros_idx[0]):
        result[index] = zeros_idx[0] - index
    for index in range(1, len(zeros_idx)):
        for between_zeros in range(zeros_idx[index - 1] + 1, zeros_idx[index]):
            result[between_zeros] = min(between_zeros - zeros_idx[index - 1],
                                        zeros_idx[index] - between_zeros)
    for index in range(zeros_idx[-1] + 1, len(array)):
        result[index] = index - zeros_idx[-1]
    return result


if __name__ == "__main__":
    length = int(input())
    array = [int(value) for value in input().strip().split()]
    print(*find_distance_to_nearest_zero(array))
