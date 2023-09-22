def fatorial(n):
    i = 0
    factorial = 1
    while i<=n+4:
        factorial = factorial*n
        n = n - 1
        i = i + 1
    return factorial