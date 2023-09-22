def qtd_divisores(n):
    """Função que calcula quantos divisores um numero n tem.
    int -> int"""
    divisores = 0
    for (i + 1) in range(n):
        if i % n == 0:
            divisores = divisores + 1
    return divisores