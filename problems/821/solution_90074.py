def fatorial(n):
    fato = 1
    for num in range(2, n + 1):
        fato *= num
    return fato