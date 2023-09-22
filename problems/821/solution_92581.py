def fatorial(n):
    f = n
    fat = 0
    while f > 0:
        if f - 1 > 0:
            fat = fat * f-1
        f = f -1
    return f