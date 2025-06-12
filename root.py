def square_root(n):
    return n**0.5


def nth_root(n, r):
    return n ** (1 / r)


if __name__ == "__main__":
    print("sqrt(16) =", square_root(16))
    print("27^(1/3) =", nth_root(27, 3))
