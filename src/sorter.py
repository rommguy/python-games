# First merge sort implementation
from typing import List
from functools import reduce
from math import floor
from multiprocessing import Pool
import time


def merge_lists(left: List[int], right: List[int]) -> List[int]:
    result = []
    left_index = 0
    right_index = 0
    right_len = len(right)
    left_len = len(left)
    while left_index < left_len and right_index < right_len:
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left_index == left_len and right_index == right_len:
        return result

    if left_index == left_len:
        return result + right[right_index:]

    if right_index == right_len:
        return result + left[left_index:]

    return []


def merge_sort(list_to_sort: List[int]) -> List[int]:
    if len(list_to_sort) <= 1:
        return list_to_sort

    middle_index = int(len(list_to_sort) / 2)
    left = list_to_sort[:middle_index]
    right = list_to_sort[middle_index:]
    return merge_lists(merge_sort(left), merge_sort(right))


def bucket_sort(list_to_sort: List[int], num_of_buckets: int) -> List[int]:
    if len(list_to_sort) == 0:
        return list_to_sort
    buckets = [[]] * num_of_buckets  # type: ignore
    max_item = max(list_to_sort)

    for i in list_to_sort:
        bucket_index = floor(num_of_buckets * i / (max_item + 1))
        buckets[bucket_index].append(i)

    for i in range(num_of_buckets):
        buckets[i] = merge_sort(buckets[i])
    return reduce(lambda accu, bucket: accu + bucket, buckets, [])


def bucket_sort_multiprocess(list_to_sort: List[int], num_of_buckets: int) -> List[int]:
    if len(list_to_sort) == 0:
        return list_to_sort
    buckets = [[] for i in range(num_of_buckets)]  # type: ignore
    max_item = max(list_to_sort)

    start = time.time()
    for i in list_to_sort:
        bucket_index = floor(num_of_buckets * i / (max_item + 1))
        buckets[bucket_index].append(i)
    print("Done sorting to buckets", time.time() - start)

    with Pool(num_of_buckets) as p:
        results = p.map(merge_sort, buckets)
        return reduce(lambda accu, bucket: accu + bucket, results, [])
