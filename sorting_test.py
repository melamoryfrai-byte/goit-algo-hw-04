import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

# ---------------- Algorithms ----------------

def bubble_sort(arr):
    a = arr[:] 
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

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
    insertion_times = []
    merge_times = []
    timsort_times = []
    bubble_times = []

    for n in sizes:
        print(f"\n--- N = {n} ---")
        data = [random.randint(0, 100000) for _ in range(n)]

        # insertion sort only for small n
        if n <= 2000:
            t_ins = timeit.timeit(lambda: insertion_sort(data), number=3) / 3.0
            insertion_times.append(t_ins)
            print(f"Insertion sort: {t_ins:.5f} sec (avg of 3)")
        else:
            insertion_times.append(np.nan)
            print("Insertion sort:  (skipped, too slow)")

        t_mer = timeit.timeit(lambda: merge_sort(data), number=3) / 3.0
        merge_times.append(t_mer)
        print(f"Merge sort:      {t_mer:.5f} sec (avg of 3)")

        t_tim = timeit.timeit(lambda: sorted(data), number=3) / 3.0
        timsort_times.append(t_tim)
        print(f"Timsort (built-in): {t_tim:.5f} sec (avg of 3)")

        t_bub = timeit.timeit(lambda: bubble_sort(data), number=3) / 3.0
        bubble_times.append(t_bub)
        print(f"Bubble sort:    {t_bub:.5f} sec (avg of 3)")

    # Convert lists to numpy arrays for plotting (NaN stays for skipped)
    ins = np.array(insertion_times, dtype=float)
    mer = np.array(merge_times, dtype=float)
    tim = np.array(timsort_times, dtype=float)
    bub = np.array(bubble_times, dtype=float)

    # Plot results
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, ins, marker='o', label='Insertion sort')
    plt.plot(sizes, mer, marker='o', label='Merge sort')
    plt.plot(sizes, tim, marker='o', label='Timsort (built-in)')
    plt.plot(sizes, bub, marker='o', label='Bubble sort')

    plt.xlabel('Input size N')
    plt.ylabel('Time (seconds, avg of 3 runs)')
    plt.title('Sorting algorithms benchmark')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # use log scale to better show differences
    plt.tight_layout()
    plt.savefig('sorting_benchmark.png')
    print("\nPlot saved to sorting_benchmark.png")
    plt.show()

if __name__ == "__main__":
    benchmark()
