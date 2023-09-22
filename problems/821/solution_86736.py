def fatorial(n):
    contador=0
    acumulador=0
    while contador<=n:
        acumulador= acumulador + n*(n-1)
    contador=contador+1
    return acumulador