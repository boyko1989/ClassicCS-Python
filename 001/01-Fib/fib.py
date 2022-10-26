from typing import Dict

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
        last, next = next, last + 1
    return next

# print(fib_m(3))

for i in range(1, 9):
    print(fib_simple(i))
