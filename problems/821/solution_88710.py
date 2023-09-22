def fatorial(n):
    fatorial = 1
    for numero in range(2, n + 1):
        fatorial *= numero
    return fatorial