def fatorial(n):
    i = 0
    factorial = 1
    while i<=n:
        factorial = factorial*(n+1)
        n = n -1
        i = i + 1
    return factorial