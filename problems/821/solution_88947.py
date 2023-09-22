def fatorial(n):
    a = 1
    while n > 0:
        a = a*n*(n-1)
        n = n - 1
    return a