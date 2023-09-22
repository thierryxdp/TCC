def fatorial(n):
    f = 1
    contador = n
    while contador != 0:
        f = f * (n*n-1)
        n = n-1
        contador = contador-1
    return f