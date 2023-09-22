def qtd_divisores(n):
    """Função que calcula a quantidade de divisores que um número pode ter;
    int/float -> int"""
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1

    return divisores