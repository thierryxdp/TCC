def fatorial(n):
    """Dado um número n, a função calcula e retorna o fatorial desse
    número.
    Parametros de entrada: int
    Retorna: int"""

    i=1
    fatorial=1

    while i<=n:
        fatorial= fatorial*i
        i+=1
    return fatorial