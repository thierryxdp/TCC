def fatorial(n):
    """Calcula o valor H,pela soma dos termos do fatorial 1/n; int=>float """
    soma = 0
    for c in range(1, n + 1):
        prod = 1
        for d in range(c, 0, -1):
            prod *= d
        soma += prod
    return soma