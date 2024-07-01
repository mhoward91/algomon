import math


def prime(x: int) -> bool:
    if x == 1:
        return False

    for x in range(2, int(math.sqrt(x)) + 1):
        if x % 2 == 0:
            return False
    return True


print([0] * 8)