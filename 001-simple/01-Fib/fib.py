from typing import Dict
from typing import Generator

memo: Dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def fib_m(n: int) -> int:
    if n not in memo:
        memo[n] = fib_m(n - 1) + fib_m(n - 2)
    return memo[n]


def fib_simple(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
    return next


def fib_gener(n: int) -> Generator[int, None, None]:
    yield 0

    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


# print(fib_m(8))

# for i in range(1, 9):
#     print(fib_gener(i))

for i in fib_gener(8):
    print(i)
