def task1(n: int) -> int:
    current = 1
    while current**2 <= n:
        current = current + 1
    return current - 1

print(task1(123))

