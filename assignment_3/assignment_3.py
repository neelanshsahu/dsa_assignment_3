# Sorting Performance Analyzer (SPA)

import time
import random

# ------------------ INSERTION SORT ------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


# ------------------ MERGE SORT ------------------
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# ------------------ QUICK SORT (FIXED 🔥) ------------------
def partition(arr, low, high):
    # RANDOM PIVOT (prevents worst case)
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)

        # Recurse on smaller side first (prevents deep recursion)
        if pi - low < high - pi:
            quick_sort(arr, low, pi - 1)
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high)
            high = pi - 1

    return arr


# ------------------ TIMING FUNCTION ------------------
def measure_time(func, arr, is_quick=False):
    data = arr.copy()

    start = time.time()

    if len(data) > 0:
        if is_quick:
            func(data, 0, len(data) - 1)
        else:
            func(data)

    end = time.time()

    return round((end - start) * 1000, 3)


# ------------------ DATASET GENERATOR ------------------
def generate_datasets():
    random.seed(42)

    sizes = [1000, 5000, 10000]
    datasets = []

    for size in sizes:
        datasets.append((size, "random", [random.randint(1, 100000) for _ in range(size)]))
        datasets.append((size, "sorted", list(range(size))))
        datasets.append((size, "reverse", list(range(size, 0, -1))))

    return datasets


# ------------------ MAIN ------------------
def main():

    print("===== CORRECTNESS CHECK =====")
    test = [5, 2, 9, 1, 5, 6]

    print("Insertion:", insertion_sort(test.copy()))
    print("Merge:", merge_sort(test.copy()))
    print("Quick:", quick_sort(test.copy(), 0, len(test) - 1))

    print("\n===== PERFORMANCE =====")
    print("Size | Type | Insertion(ms) | Merge(ms) | Quick(ms)")
    print("-" * 65)

    datasets = generate_datasets()

    for size, dtype, arr in datasets:
        t1 = measure_time(insertion_sort, arr)
        t2 = measure_time(merge_sort, arr)
        t3 = measure_time(quick_sort, arr, True)

        print(f"{size} | {dtype} | {t1} | {t2} | {t3}")


if __name__ == "__main__":
    main()