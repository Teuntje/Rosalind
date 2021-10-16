def fibonacci(k, n):
    """Calculate fibonacci, return the 'number of rabbits'"""
    fibonacci_reeks = []
    for i in range(n):
        if i == 0:
            fibonacci_reeks.append(1)
        elif i == 1:
            fibonacci_reeks.append(1)
        elif i != 0 and i != 1:
            next_num = fibonacci_reeks[i-1] + (fibonacci_reeks[i-2]*k)
            fibonacci_reeks.append(next_num)
    return fibonacci_reeks


if __name__ == "__main__":
    n = 35
    k = 4
    fib = fibonacci(k, n)
    print(fib[-1])
