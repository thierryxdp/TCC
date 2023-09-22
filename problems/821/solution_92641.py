def fatorial(n):
    i = 1
    acumulador = 1
    while i <= n:
        acumulador = acumulador * i
        i = i + 1
    return acumulador