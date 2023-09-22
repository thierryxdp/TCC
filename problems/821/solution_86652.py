def fatorial(n):
    """essa função recebe um número e retorna o fatorial do mesmo.
    Entrada: inteiro. Saida: Inteiro"""
    b = 1
    while n > 0:
        b = b*n
        n = n-1
    return b