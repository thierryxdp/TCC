def qtd_divisores(numero):
    """Função que irá contar quntos divisores um determinado número tem."""
    soma = 0
    for possivel_divisor in range(1, numero + 1):
        if numero % possivel_divisor == 0:
            soma = soma + 1
    return soma