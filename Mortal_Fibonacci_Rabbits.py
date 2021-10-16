def fibonacci(k, n, m):
    """Calculate the mortal fibonacci when the rabbits die after month n"""
    fibonacci_reeks = []
    for i in range(n):
        if i == 0:
            fibonacci_reeks.append(1)
        elif i == 1:
            fibonacci_reeks.append(1)
        elif i != 0 and i != 1:
            if i < m:
                next_num = fibonacci_reeks[i-1] + (fibonacci_reeks[i-2]*k)
            if i == m:
                next_num = fibonacci_reeks[i-1] + (fibonacci_reeks[i-2]*k) - 1
            elif i > m:
                next_num = fibonacci_reeks[i-1] + (fibonacci_reeks[i-2]*k) - fibonacci_reeks[i-(m+1)]
            fibonacci_reeks.append(next_num)
    return fibonacci_reeks


if __name__ == "__main__":
    n = 93
    k = 1
    m = 17
    fib = fibonacci(k, n, m)
    print(fib[-1])
