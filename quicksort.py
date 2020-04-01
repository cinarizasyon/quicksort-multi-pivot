import random
from datetime import datetime


def get_pivot(arr, choice='median'):
    if not arr:
        return 0
    length = len(arr)
    if length == 1:
        return arr[0]

    if choice == 'median':
        median = int(length / 2)
        return (arr[median - 1] + arr[median]) / 2 if length % 2 == 0 else arr[median]
    elif choice == 'random':
        return arr[random.randint(0, length - 1)]
    elif choice == 'first':
        return arr[0]
    elif choice == 'last':
        return arr[-1]
    else:
        raise Exception(
            'Please use a valid pivot choice. (median, random, first, last)')


def partition(array, pivot_choice='median'):
    pivot = get_pivot(array, choice=pivot_choice)
    lt, eq, gt = [], [], []
    for item in array:
        if item < pivot:
            lt.append(item)
        elif item > pivot:
            gt.append(item)
        else:
            eq.append(item)
    return lt, eq, gt


def quick_sort(array, length, sorted_array=[]):
    if not array or len(sorted_array) == length:
        return
    if len(array) == 1:
        sorted_array.extend(array)
        return
    lt, eq, gt = partition(array)
    quick_sort(lt, length, sorted_array)
    sorted_array.extend(eq)
    quick_sort(gt, length, sorted_array)
    return sorted_array


def main():
    sample = [random.randint(1, 10) for i in range(100000)]
    t1 = datetime.now()
    result = quick_sort(sample, len(sample))
    t2 = datetime.now()
    print(t2-t1)
    print(result[:10])


if __name__ == "__main__":
    main()
