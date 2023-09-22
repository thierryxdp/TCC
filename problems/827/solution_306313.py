def qtd_divisores(n):
    """Função que conta quantos divisores um numero possui.
    Parametros: int->int"""
    soma = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            soma += n
    return soma