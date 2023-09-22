def fatorial(n):
    i = n*(n-1)
    x = 0
    while i < n:
        x = x*n
        i += -1
    return x