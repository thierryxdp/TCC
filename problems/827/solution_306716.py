def qtd_divisores(numero):
    """ Função que conta quantos divisores um número tem;
        int -> int"""
    divisores = 0
    for i in range(1,numero+1):
        if numero%i == 0:
            divisores = divisores + 1
    return divisores