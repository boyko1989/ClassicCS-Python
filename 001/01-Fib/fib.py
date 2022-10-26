from typing import Dict
memo: Dict[int, int] = {0:0,1:1}


def fib(n: int) -> int:
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)

def fib_m(n: int) -> int:
    if n not in memo:
        memo[n] = fib_m(n - 1) + fib_m(n - 2)
    return memo[n]


# print(fib_m(3))

for i in range(1, 9):
     print(fib_m(i))


