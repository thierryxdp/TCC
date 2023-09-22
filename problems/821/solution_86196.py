def fatorial(n):
    """retorna o fatorial do numero de entrada n"""
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num