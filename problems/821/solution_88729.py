def fatorial(n):
    ''''''
    acumulador = 1
    lista = list(range(n))
    del lista[0]
    for x in lista:
        acumulador = acumulador*x
    return acumulador