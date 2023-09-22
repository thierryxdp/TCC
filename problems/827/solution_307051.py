def qtd_divisores(n):
    """função que retorna a quantidade de divisores de um numero
    int -> int"""
    divisores = 0
    for d in range(1,n):
        if n % d == 0:
            divisores = divisores + 1
    return divisores