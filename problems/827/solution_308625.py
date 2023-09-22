def qtd_divisores(n: int) -> int:
    """ funçao que calcula e retorna a quantidade de divisores que um numero tem;int,int->int"""
    contador = 0
    for i in range(1, n + 1):
        if (n % i) == 0:
            contador += 1
    return contador