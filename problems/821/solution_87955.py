def fatorial(n):
    f = n
    contador = 1
    while contador > 1:
        f = f * (n*n-1)
        n = n-1
        contador = contador-1
    return f