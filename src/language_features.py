from typing import List, Callable


def generate_closure_updater() -> Callable[[int], List[int]]:
    my_list: List[int] = []

    def update_closure(num: int) -> List[int]:
        my_list.append(num)
        return my_list

    return update_closure


def increment_num(num: int) -> int:
    return num + 1
