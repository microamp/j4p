def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


if __name__ == "__main__":
    f = fib()
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
