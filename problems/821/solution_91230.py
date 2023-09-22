def fatorial(n):
    total = n
    while n > 0:
        n = n - 1
        if n != 0:
            total = total * n
    return total