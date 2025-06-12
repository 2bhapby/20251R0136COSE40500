def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


if __name__ == "__main__":
    print("10 / 2 =", divide(10, 2))
