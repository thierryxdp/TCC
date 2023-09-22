def fatorial(n):
    contador = 1
    acumulador = 1
    while contador <= n:
        if contador < n: 
            acumulador = acumulador*(n-contador)
        else:
            acumulador = acumulador*n
        contador = contador + 1
    return acumulador