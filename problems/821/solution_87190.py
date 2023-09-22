def fatorial(n):
    """Função que calcula o fatorial de um número
    int -> int"""

    fatorial = 1
    i = 2

    while i <= n:
        fatorial = fatorial * i
        i = i + 1

    return fatorial