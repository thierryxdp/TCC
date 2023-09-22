def qtd_divisores(n):
    ''''''
    acumulador = 0
    for i range(n):
        if n % n == 0:
            acumulador = acumulador + 1
    return acumulador