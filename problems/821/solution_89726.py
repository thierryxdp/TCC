def fatorial(n):
    """Função que calcula e retorna o valor do fatorial do parâmetro de entrada (n).
    int -> int"""
    fatorial = 1
    i = n * (n-1)
    while n >= 1:
        fatorial = fatorial * n
        n = n-1
    return fatorial