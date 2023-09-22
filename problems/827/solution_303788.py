def qtd_divisores(n):
    """dado um número inteiro positivo n, calcula e retorna o número de divisores (positivos) de n; int -> int"""
    divisores = []
    for i in range(1, n+1):
        if n%i == 0:
            divisores += [i]
    return len(divisores)