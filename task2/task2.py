def task2(i1: int, i2: int) -> int:
    if i2 > i1:
        current = i1
    else:
        current = i2

    while current > 0:
        i1Div = int(i1 / current)
        i2Div = int(i2 / current)

        i1Comp = i1Div * current
        i2Comp = i2Div * current

        if i1Comp != i1:
            current -= 1
            continue
        if i2Comp != i2:
            current -= 1
            continue

        return current

    
print(task2(36, 64))