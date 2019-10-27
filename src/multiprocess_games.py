import multiprocessing
from datetime import datetime, timedelta
from typing import Any
import threading


def wait_seconds(seconds_to_wait: int) -> None:
    start_time = datetime.now()
    delta = datetime.now() - start_time
    while delta.seconds < seconds_to_wait:
        delta = datetime.now() - start_time


def print_time_and_wait_ten_seconds() -> str:
    start_time = datetime.now()
    wait_seconds(3)
    return f"PID{multiprocessing.current_process().pid}. Started at {str(start_time)}"


def main_func_apply() -> None:
    with multiprocessing.Pool(processes=4) as pool:
        print(pool.apply(print_time_and_wait_ten_seconds))
        print(pool.apply(print_time_and_wait_ten_seconds))


def main_func_apply_async() -> None:
    def print_res(bla: Any) -> None:
        print("res ready")
        print(bla.get())

    with multiprocessing.Pool(processes=4) as pool:
        res = pool.apply_async(print_time_and_wait_ten_seconds)
        res2 = pool.apply_async(print_time_and_wait_ten_seconds)
        res3 = pool.apply_async(print_time_and_wait_ten_seconds)
        res4 = pool.apply_async(print_time_and_wait_ten_seconds)
        res5 = pool.apply_async(print_time_and_wait_ten_seconds)
        res6 = pool.apply_async(print_time_and_wait_ten_seconds)
        res7 = pool.apply_async(print_time_and_wait_ten_seconds)
        res8 = pool.apply_async(print_time_and_wait_ten_seconds)
        res9 = pool.apply_async(print_time_and_wait_ten_seconds)

        print(res.get(timeout=20))
        print(res2.get(timeout=20))
        print(res3.get(timeout=20))
        print(res4.get(timeout=20))

        print("************")

        print(res5.get(timeout=20))
        print(res6.get(timeout=20))
        print(res7.get(timeout=20))
        print(res8.get(timeout=20))

        print("************")

        print(res9.get(timeout=20))


if __name__ == "__main__":
    main_func_apply_async()
