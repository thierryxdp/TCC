def qtd_divisores(numero):
    """ função que recebe um número e conta quantos divisores um número tem;
    int -> int"""
    soma = 0
    for elemento in range(1,11):
        if elemento%numero == 0:
            soma = soma + 1
    return soma