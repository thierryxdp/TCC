def fatorial(n):
    i = 0
    factorial = 2
    while i<=n:
        factorial = factorial*n
        n = n - 1
        i = i + 1
    return factorial