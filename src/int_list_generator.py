from random import randint


def generate_int_list(length: int):
    return [randint(0, length * 10) for i in range(length)]
