def fatorial(n):
    fatoracao = n
    while n > 1:
        fatoracao *= n - 1
        n -= 1

    return fatoracao