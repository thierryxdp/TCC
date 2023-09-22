def fatorial(n):
    c = n
    while c > 1:
        a = n - 1
        n = n * a
        c = c - 1
    return n