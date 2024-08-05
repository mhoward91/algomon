# Use when able to make a binary decision to shrink the search range
from typing import List


# time O(log(n)) where n = len(arr), space O(1)
def bin_search(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# time O(log(n)) where n = len(arr) space O(log(n))
def bin_search_rec(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    return bin_search_rec_helper(arr, target, left, right)


def bin_search_rec_helper(
        arr: List[int], target: int, left: int, right: int) -> int:
    if not left <= right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return bin_search_rec_helper(arr, target, mid + 1, right)
    else:
        return bin_search_rec_helper(arr, target, left, mid - 1)


# look for first True in boolean array ordered with F values before T values
# find the feasible function that returns False up until the first True
# then the first true is the answer!
# replace the if arr[mid] line with the feasible function!
# this works as long as the array is ordered, strictly increasing OR decreasing
def bin_search_bool(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_idx = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_idx = mid  # keep track of the last True position
            right = mid - 1
        else:
            left = mid + 1

    return boundary_idx


def bin_search_monotonic(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary_idx = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:  # this is the 'feasible function' - ret. bool
            if arr[mid] == target:
                boundary_idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_idx


def find_min_rotated(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_idx = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:  # min value in pivot array in lower half
            boundary_idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_idx


def find_peak_element(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_idx = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1] or mid == len(arr) - 1:
            boundary_idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_idx


# advanced algorithm - splitting newspapers among coworkers, reading in as
# quick as time as possible - feasible in this case is a full function
# is it possible to distribute newspapers to coworkers in this (mid) time?
# time is O(n log m), space O(1)
def feasible(
    newspaper_read_times: List[int],
    num_coworkers: int,
    limit: int
) -> bool:
    time, num_workers = 0, 0
    for read_time in newspaper_read_times:
        if time + read_time > limit:
            time = 0
            num_workers += 1
        time += read_time

    if time != 0:
        num_workers += 1

    return num_workers <= num_coworkers


def newspapers_split(
        newspapers_read_times: List[int], num_coworkers: int) -> int:
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if feasible(newspapers_read_times, num_coworkers, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
