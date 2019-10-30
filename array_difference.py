

def min_max_diff(array):
    max_number = array[0]
    min_number = array[0]

    for num in array:
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num

    print(max_number)
    print(min_number)

    return max_number - min_number


def returnMinMaxDiff(array):

    array_sorted = sorted(array)

    min = array_sorted[0]

    max = array_sorted[-1]

    print(min)
    print(max)

    return max - min


if __name__ == '__main__':
    print(min_max_diff([15, 22, 84, 14, 88, 23]))

    print("-" * 6)
    print(returnMinMaxDiff([15, 22, 84, 14, 88, 23]))
