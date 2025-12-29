def task4(n: int) -> int:
    current = n
    while current <= 1000:
        if isPrime(current):
            return current
        current = current + 1

def isPrime(n: int) -> bool:
    current = 2
    while current**2 <= n:

        div = int(n / current)
        remainder = n - div * current
        if remainder == 0:
            return False
        current = current + 1
    return True

print(task4(233))

