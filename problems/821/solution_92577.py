def fatorial(n):
    f = 0
    fat = n
    while n > 0:
        if n - 1 > 0:
            f = fat * n-1
        n = n -1
        fat = n * n-1
    return f