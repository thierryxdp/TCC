def qtd_divisores (numero):
    """função que dado um número, conte quantos divisores tal número tem.
    int -> int"""
    soma = 0
    for d in range(1,numero+1):
        if numero % d == 0:
            soma = soma + 1
    return soma