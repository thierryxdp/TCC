def fatorial(n):
    c = 0
    d = 1
    while c < n:
        d *= (c + 1)
        c += 1
    return d