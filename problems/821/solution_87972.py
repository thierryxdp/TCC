def fatorial(n):
    """Função que recebe um numero e retorna seu fatorial"""
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat