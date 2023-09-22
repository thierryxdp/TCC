def soma_h(n):
    """Recebe um número inteiro n e retorna a somatória de 1/i, em que i = {1,2,
    3,..., n}, com 2 casas decimais de aproximação.

    int -> int"""
    if n == 1:
        return 1
    else:
        return round(1/n + soma_h(n-1), 2)