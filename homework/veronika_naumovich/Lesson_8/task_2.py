import sys
sys.set_int_max_str_digits(0)


def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


positions = [5, 200, 1000, 100000]
count = 0

for n in fib():
    count += 1
    if count in positions:
        print(f"{count}-е число Фибоначчи: {n}")
        if count >= max(positions):
            break
