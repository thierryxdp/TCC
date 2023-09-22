def fatorial(n):
    f = n
    fat = n
    while f > 0:
        if f - 1 > 0:
            fat = fat * f-1
        f = f -1
        fat = fat * n-1
    return f