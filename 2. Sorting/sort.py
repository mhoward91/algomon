# stable sorting algorithm means relative order is maintained following sort
#   if two elements have the same value

# insertion sort & bubble sort good for 'almost sorted' algorithms

from typing import List


# enumerate through the unsorted list
# swap elements if the el to the right is smaller than the el to the left
# check this at each index position down to 1 (greater than zero)
# time O(n^2) - stable & in-place
def insertion_sort(lst: List[int]) -> List[int]:
    for i, _ in enumerate(lst):
        current = i
        while current > 0 and lst[current] < lst[current - 1]:
            lst[current], lst[current - 1] = lst[current - 1], lst[current]
            current -= 1

    return lst


# find smallest item from unsorted pile
# add it to the front of the unsorted pile, where it becomes part of the
#   the sorted pile
# time O(n^2) - not stable but in-place
def selection_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]


# for each pass, use a pointer to point at first element of list
# for each cycle, compare to next element & swap if current item is greater
# increment by 1 until reaching end of list
# list is sorted if, during a pass, no swap occurs
# time O(n^2) - stable & in-place
def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in reversed(range(n)):
        swapped = False
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            return lst
    return lst
