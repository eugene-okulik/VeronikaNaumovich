def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


positions = [5, 200, 1000, 100000]
count = 0

for n in fib():
    count += 1
    if count == positions[0]:
        print(f"{count}-е число Фибоначчи: {n}")
        positions.pop(0)
        if not positions:
            break
