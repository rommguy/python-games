from random import randint
from typing import List


def generate_int_list(length: int) -> List[int]:
    return [randint(0, length * 10) for i in range(length)]
