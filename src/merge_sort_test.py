from src.sorter import merge_lists, merge_sort, bucket_sort, bucket_sort_multiprocess
from src.int_list_generator import generate_int_list
import time


def test_merge_lists():
    assert merge_lists(left=[], right=[1, 2]) == [1, 2], "ignore empty lists"
    assert merge_lists([1, 2], []) == [1, 2], "ignore empty lists"
    assert merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6], "Lists should be merged"

    assert merge_lists(left=[1, 5], right=[3, 4]) == [1, 3, 4, 5], "Should merge lists"
    assert merge_lists([1, 3, 5, 7, 8, 9], [2, 4]) == [1, 2, 3, 4, 5, 7, 8, 9], "Should merge lists"


def test_merge_sort():
    list_to_sort = [7, 1, 2, 9, 10, 5, 5, 6]
    assert merge_sort([]) == [], "Should return an empty list"
    assert merge_sort(list_to_sort) == sorted(list_to_sort), "Should sort the given list"


def test_bucket_sort():
    list_to_sort = generate_int_list(10000)
    assert bucket_sort([], 10) == [], "Should return an empty list"
    assert bucket_sort(list_to_sort, 3) == sorted(list_to_sort), "Should sort the given list"

    assert bucket_sort_multiprocess(list_to_sort, 10) == sorted(list_to_sort), "Should sort the given list"


def test_bucket_sort_multiprocess():
    start = time.time()
    print("Start test - multi")
    list_to_sort = generate_int_list(100000)
    bucket_sort_multiprocess(list_to_sort, 12)
    print("End test - multi", time.time() - start)

    start_single = time.time()
    print("Start test - single")
    # bucket_sort(list_to_sort, 12)
    print("End test - single", time.time() - start_single)
