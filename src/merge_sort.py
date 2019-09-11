# First merge sort implementation
from typing import List


def merge_lists(left: List[int], right: List[int]) -> List[int]:
    result = []
    left_index = 0
    right_index = 0
    right_len = len(right)
    left_len = len(left)
    while left_index < left_len and right_index < right_len:
        if left[left_index] <= right[right_index]:
            result = [*result, left[left_index]]
            left_index += 1
        else:
            result = [*result, right[right_index]]
            right_index += 1

    if left_index == left_len and right_index == right_len:
        return result

    if left_index == left_len:
        return [*result, *right[right_index:]]

    if right_index == right_len:
        return [*result, *left[left_index:]]
