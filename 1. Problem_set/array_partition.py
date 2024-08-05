# time O(n log(n)) due to sorting, space, O()
def array_partition(arr: list) -> int:
    return sum(sorted(arr)[::2])
