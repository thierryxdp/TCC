def fatorial(n):
    f = 0
    fat = n
    while n > 0:
        if n > 0:
            f = fat * n-1
        n = n -1
        fat = f
    return f