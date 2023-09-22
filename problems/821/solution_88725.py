def fatorial(n):
    ''''''
    acumulador = 1
    for x in range(n + 1):
        acumulador = acumulador*x
    return acumulador