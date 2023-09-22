def qtd_divisores(n):
    ''''''
    acumulador = 0
    for i in range(1,n):
        if n % i == 0:
            acumulador = acumulador + 1
    return acumulador