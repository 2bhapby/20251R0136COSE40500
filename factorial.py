def factorial(n):
    if n < 0:
        return "Error: Negative number"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
