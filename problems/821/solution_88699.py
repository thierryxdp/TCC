def fatorial(n):
    contador = 0
    fac = n - 1
    if fac == 0:
        return 1
    while contador < n:
        fac = (n-contador)*fac
        contador = contador + 1
    return fac//(n-1)