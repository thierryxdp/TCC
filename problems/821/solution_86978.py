def fatorial(n):
    if n == 0:
        return 1
    if n < 0:
        return -1
    fat = 1
    while n != 1:
        fat *= n
        n -= 1
    return fat