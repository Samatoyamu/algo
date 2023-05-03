# ID 85026845
def quick_sort(array):
    def partition(array, left, right):
        smallest_value = left - 1
        for value in range(left, right):
            if array[value] <= array[right]:
                smallest_value += 1
                array[smallest_value], array[value] = (array[value],
                                                       array[smallest_value])
        array[smallest_value + 1], array[right] = (array[right],
                                                   array[smallest_value + 1])
        return smallest_value + 1

    def sorting(array, left, right):
        if left < right:
            partitions = partition(array, left, right)
            sorting(array, left, partitions - 1)
            sorting(array, partitions + 1, right)
    sorting(array, 0, len(array) - 1)


def participant_sort(login, problem, fine):
    return -int(problem), int(fine), login


if __name__ == "__main__":
    length = int(input())
    participant = [participant_sort(*input().split()) for _ in range(length)]
    quick_sort(participant)
    print(*(login for _, _, login in participant), sep="\n")
