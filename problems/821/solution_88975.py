def fatorial(n):
    """função que retorna o fatorial de um numero
    int -> int"""
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num