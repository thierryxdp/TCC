def fatorial(numero):
    """Calcula e retorna o fatorial de um numero fornecido na entrada
    int -> int
    """
    i = 1
    fatorial = 1
    while i <= numero:
        fatorial = fatorial * i
        i += 1
    return fatorial