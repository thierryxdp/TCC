def qtd_divisores(numero):
    '''Função que dado um número, quantifica quantos divisores esse número tem;
    int -> int'''
    soma_divisores = 0
    for div in range(1,numero):
        if numero % div == 0:
            soma_divisores = soma_divisores + 1
    return soma_divisores