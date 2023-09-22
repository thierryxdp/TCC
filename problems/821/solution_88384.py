def fatorial(n):
    r = 1
    for i in range(n):
        r = r * n
        n = n-1
    return r