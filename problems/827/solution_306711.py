def qtd_divisores(numero):
    """ Função que conta quantos divisores um número tem;
        float -> int"""
    i = 0
    divisores = 0
    while i < numero+1:
        if numero%i == 0:
            divisores = divisores + 1
        i = i + 1
    return divisores