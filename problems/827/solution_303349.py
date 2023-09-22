def qtd_divisores(numero):
    ''' função que conta quantos divisores um número tem.
    entrada: int;
    saída: int'''
    acumulador = 0
    for i in range(número + 1):
        if numero % i == 0:
            acumulador = acumulador + 1
    return acumulador