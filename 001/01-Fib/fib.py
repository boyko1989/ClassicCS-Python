def fib(n: int) -> int:
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


# print(fib(3))

for i in range(1, 9):
    print(fib(i))
