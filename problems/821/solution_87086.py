def fatorial(n):
    """Funcao que retorna o fatorial de um numero inteiro."""
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num