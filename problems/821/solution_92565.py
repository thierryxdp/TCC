def fatorial(n):
    fat = n
    f = 0
    while fat > 0:
        if n-1 > 0:
            f = fat * n-1
        fat = fat -1
    return fat