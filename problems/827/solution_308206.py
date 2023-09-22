def qtd_divisores(n):
    """Dado um número n, retorna a quantidade de divisores que esse
    número tem."""
    contagem = 0
    for i in range(1, n+1):
        if n % i == 0:
            contagem += 1
    return contagem