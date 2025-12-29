def task3(n: int) -> None:
    current = n
    stack = []

    while current >= 0:

        res = int(current / 3)
        remainder = current - res * 3
        stack.append(remainder)
        current = res

        if len(stack) == 7:
            break

    while stack != []:
        print(stack.pop(), end=" ")

task3(377)

