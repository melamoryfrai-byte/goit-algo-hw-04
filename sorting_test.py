import random
import timeit

# ---------------- Algorithms ----------------

def insertion_sort(arr):
    a = arr[:] 
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i+=1
        else:
            merged.append(right[j]); j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# ---------------- Benchmark ----------------

sizes = [1000, 2000, 5000]

def benchmark():
    for n in sizes:
        print(f"\n--- N = {n} ---")
        
        data = [random.randint(0, 100000) for _ in range(n)]

        # insertion sort only for small n
        if n <= 2000:
            t_ins = timeit.timeit(lambda: insertion_sort(data), number=3)
            print(f"Insertion sort: {t_ins:.5f} sec")
        else:
            print("Insertion sort:  (skipped, too slow)")

        t_mer = timeit.timeit(lambda: merge_sort(data), number=3)
        print(f"Merge sort:      {t_mer:.5f} sec")

        t_tim = timeit.timeit(lambda: sorted(data), number=3)
        print(f"Timsort (built-in): {t_tim:.5f} sec")


if __name__ == "__main__":
    benchmark()
