import argparse
import random
import copy
import math
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# -------------------- State helpers --------------------

def _state(arr, comps=None, swaps=None):
    return (arr.copy(), tuple(comps) if comps else (), tuple(swaps) if swaps else ())


# -------------------- Generators for algorithms --------------------

def gen_bubble(arr):
    A = arr.copy()
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            yield _state(A, comps=(j, j + 1))
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                yield _state(A, swaps=(j, j + 1))
    yield _state(A)


def gen_insertion(arr):
    A = arr.copy()
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            yield _state(A, comps=(j, j + 1))
            A[j + 1] = A[j]
            yield _state(A, swaps=(j, j + 1))
            j -= 1
        A[j + 1] = key
        yield _state(A)
    yield _state(A)


def gen_selection(arr):
    A = arr.copy()
    n = len(A)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            yield _state(A, comps=(min_idx, j))
            if A[j] < A[min_idx]:
                min_idx = j
                yield _state(A, comps=(min_idx,))
        if min_idx != i:
            A[i], A[min_idx] = A[min_idx], A[i]
            yield _state(A, swaps=(i, min_idx))
    yield _state(A)


def gen_shell(arr):
    A = arr.copy()
    n = len(A)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                yield _state(A, comps=(j, j - gap))
                A[j] = A[j - gap]
                yield _state(A, swaps=(j, j - gap))
                j -= gap
            A[j] = temp
            yield _state(A)
        gap //= 2
    yield _state(A)


def gen_merge(arr):
    A = arr.copy()
    n = len(A)

    def merge(l, m, r):
        left = A[l : m + 1]
        right = A[m + 1 : r + 1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            yield _state(A, comps=(k,))
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
            yield _state(A)
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
            yield _state(A)
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
            yield _state(A)

    def _sort(l, r):
        if l >= r:
            return
        m = (l + r) // 2
        yield from _sort(l, m)
        yield from _sort(m + 1, r)
        yield from merge(l, m, r)

    if n:
        yield from _sort(0, n - 1)
    yield _state(A)


def gen_quick3(arr):
    A = arr.copy()

    def _quicksort(lo, hi):
        if lo >= hi:
            return
        pivot = A[lo]
        lt = lo
        i = lo + 1
        gt = hi
        while i <= gt:
            yield _state(A, comps=(i,))
            if A[i] < pivot:
                A[lt], A[i] = A[i], A[lt]
                lt += 1
                i += 1
                yield _state(A, swaps=(lt - 1, i - 1))
            elif A[i] > pivot:
                A[i], A[gt] = A[gt], A[i]
                gt -= 1
                yield _state(A, swaps=(i, gt + 1))
            else:
                i += 1
        yield from _quicksort(lo, lt - 1)
        yield from _quicksort(gt + 1, hi)

    if len(A):
        yield from _quicksort(0, len(A) - 1)
    yield _state(A)


def gen_heap(arr):
    A = [0] + arr.copy()  # 1-based helper
    n = len(A) - 1

    def sift_down(start, end):
        root = start
        while root * 2 <= end:
            child = root * 2
            if child + 1 <= end and A[child] < A[child + 1]:
                child += 1
            if A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                yield _state(A[1:], swaps=(root - 1, child - 1))
                root = child
            else:
                return

    # build heap
    for start in range(n // 2, 0, -1):
        yield from sift_down(start, n)
    # repeatedly extract
    end = n
    while end > 1:
        A[1], A[end] = A[end], A[1]
        yield _state(A[1:], swaps=(0, end - 1))
        end -= 1
        yield from sift_down(1, end)
    yield _state(A[1:])


def gen_radix_lsd(arr, base=10):
    A = arr.copy()
    if not A:
        yield _state(A)
        return
    maxval = max(A)
    exp = 1
    while maxval // exp > 0:
        buckets = [[] for _ in range(base)]
        for x in A:
            d = (x // exp) % base
            buckets[d].append(x)
        # yield bucket state (concise): we flatten and produce intermediate state after bucket gather
        newA = []
        for b in buckets:
            newA.extend(b)
        A = newA
        yield _state(A)
        exp *= base
    yield _state(A)


# -------------------- Visualization --------------------

def visualize(generator, arr, interval=200, title='Sort Visualization', savepath=None):
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(arr)), arr, align='center', color='skyblue')
    ax.set_xlim(-0.5, max(5, len(arr) - 0.5))
    maxv = max(arr) if arr else 1
    ax.set_ylim(0, maxv * 1.1)

    def update(frame):
        A, comps, swaps = frame
        for rect, val in zip(bar_rects, A):
            rect.set_height(val)
            rect.set_color('skyblue')
        # color comparisons
        for idx in comps:
            if 0 <= idx < len(bar_rects):
                bar_rects[idx].set_color('red')
        # color swaps
        for idx in swaps:
            if 0 <= idx < len(bar_rects):
                bar_rects[idx].set_color('green')
        return bar_rects

    ani = animation.FuncAnimation(fig, update, frames=generator, interval=interval, repeat=False)

    if savepath:
        try:
            ani.save(savepath, writer='ffmpeg')
            print(f'Saved animation to {savepath}')
        except Exception as e:
            print('Failed to save animation:', e)
            print('Attempting to show interactively...')
            plt.show()
    else:
        plt.show()


# -------------------- CLI --------------------

ALG_MAP = {
    'bubble': gen_bubble,
    'insertion': gen_insertion,
    'selection': gen_selection,
    'shell': gen_shell,
    'merge': gen_merge,
    'quick3': gen_quick3,
    'heap': gen_heap,
    'radix': gen_radix_lsd,
}


def main():
    p = argparse.ArgumentParser(description='Sorting algorithm visualizer')
    p.add_argument('--algo', choices=sorted(ALG_MAP.keys()), default='bubble')
    p.add_argument('--size', type=int, default=40, help='number of elements')
    p.add_argument('--maxval', type=int, default=100, help='maximum element value')
    p.add_argument('--seed', type=int, default=None)
    p.add_argument('--interval', type=int, default=80, help='animation interval ms')
    p.add_argument('--save', type=str, default=None, help='optional output file to save (mp4)')
    args = p.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    # generate array (allow duplicates to show stability differences)
    arr = [random.randint(1, args.maxval) for _ in range(args.size)]

    gen = ALG_MAP[args.algo](arr)
    title = f"{args.algo} (n={len(arr)})"
    visualize(gen, arr, interval=args.interval, title=title, savepath=args.save)


if __name__ == '__main__':
    main()
