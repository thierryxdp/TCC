def fatorial(n):
    if n == 0:
        return 1
    mult = 1
    while n > 0:
        mult *= n
        n -= 1
    return mult