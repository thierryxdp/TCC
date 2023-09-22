def fatorial(n):
    f = ()
    fat = n
    while n > 0:
        if n - 1 > 0:
            f = fat * n-1
        n = n -1
        fat = f
    return f