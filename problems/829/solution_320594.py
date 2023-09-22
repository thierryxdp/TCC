def soma_h(n):
    """Recebe um número inteiro n e retorna a somatória h de 1/i, em que i = {1,2,
    3,..., n}, com 2 casas decimais de aproximação.

    int -> int"""
    h = 0
    for i in range(1, n+1):
        h += 1/i
    return round(h, 2)