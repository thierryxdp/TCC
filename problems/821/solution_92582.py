def fatorial(n):
    f = n
    fat = 0
    while f > 0:
        if f - 1 > 0:
            fat = f * n-1
        f = f -1
        n = n-1
    return f