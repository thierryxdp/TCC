def fatorial(n):
    f = n -1
    fat = n
    while f > 0:
        if f - 1 > 0:
            fat = fat * f-1
        f = f -1
        n = n-1
    return fat