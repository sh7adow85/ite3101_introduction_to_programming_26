from typing import List


def product(seq: List[int]) -> List[int]:
    result = 1
    for item in seq:
        result *= item
    return result