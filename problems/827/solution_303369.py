def qtd_divisores(numero):
    ''' função que conta quantos divisores um número tem.
    entrada: int;
    saída: int'''
    acumulador = 0
    for indice in range(1,numero + 1):
        if numero % indice == 0:
            acumulador = acumulador + 1
    return acumulador