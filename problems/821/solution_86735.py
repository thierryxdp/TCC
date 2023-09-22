def fatorial(n):
    contador=0
    acumulador=0
    while contador<n:
        acumulador= acumulador + n*(n-1)
        contador+=1
    return acumulador