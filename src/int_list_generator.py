from random import randint


def generate_int_list(length: int):
    return [randint(0, length) for i in range(length)]
