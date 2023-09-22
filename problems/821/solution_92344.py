def fatorial(n):
    mult = 1
    for m in range(1, n):
        m = mult * m
        fatn = n * m
    return fatn
    if n == 1:
        return 1