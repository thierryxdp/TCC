def fatorial(n):
    ''''''
    acumulador = 1
    lista = range(10)
    del lista[0]
    for x in range(n + 1):
        acumulador = acumulador*x
    return acumulador