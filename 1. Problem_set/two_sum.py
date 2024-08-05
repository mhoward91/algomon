from typing import List

nums = [7, 1, 15, 2]
target = 17


# O(n^2) time
def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    for i in range(4):
        for y in range(4):
            if i != y:
                if nums[i] + nums[y] == target:
                    return [i, y]


# O(n) time & space
def two_sum(nums: List[int], target: int) -> List[int]:
    hash_tbl = dict()
    for idx, num in enumerate(nums):
        difference = target - num
        if difference in hash_tbl:
            return [hash_tbl[difference], idx]
        hash_tbl[num] = idx


print(two_sum_brute_force(nums, target))
print(two_sum(nums, target))
