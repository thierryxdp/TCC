def fatorial(n):
    c = 0
    d = 1
    for c in range(n):
        d *= (c + 1)
        c += 1
    return d