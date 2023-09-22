def qtd_divisores(n):
    ''''''
    acumulador = 0
    for i in range(n):
        if n % 1 == 0:
            acumulador = acumulador + 1
    return acumulador