def qtd_divisores(numero):
    """Retorna a quantidade de divisores que um número tem;
    int -> int"""
    soma = 0
    for i in range (1,numero+1):
        if numero % i == 0:
            soma += 1
    return soma