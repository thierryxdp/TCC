def fatorial(n):
    contador=1
    acumulador=1
    while contador<=n:
        acumulador= acumulador*contador
        contador=contador+1
    return acumulador