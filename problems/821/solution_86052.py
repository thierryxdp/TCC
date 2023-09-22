def fatorial(n):
    """Função que calcula o fatorial de determinado número.
       Onde: "n" - é o número que se deseja calcular o fatorial.
    int --> int """
    fatorial = 1
    while n != 1:
        fatorial *= n
        n -= 1
    return fatorial