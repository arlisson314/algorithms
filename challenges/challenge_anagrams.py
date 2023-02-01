def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]

    """L = left index, R = right index"""
    L, R = 0, 0

    for index in range(start, end):
        if L >= len(left):
            arr[index] = right[R]
            R += 1
        elif R >= len(right):
            arr[index] = left[L]
            L += 1
        elif left[L] < right[R]:
            arr[index] = left[L]
            L += 1
        else:
            arr[index] = right[R]
            R += 1


def is_anagram(first_string, second_string):
    list1 = [*first_string.lower()]
    list2 = [*second_string.lower()]

    merge_sort(list1)
    merge_sort(list2)

    first_string = "".join(list1)
    second_string = "".join(list2)

    if not first_string or not second_string:
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)
