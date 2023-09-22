def qtd_divisores(n):
    """Função que calcula quantos divisores um numero n tem.
    int -> int"""
    divisores = 0
    for i in range(n):
        if (i+1) % n == 0:
            divisores = divisores + 1
    return divisores