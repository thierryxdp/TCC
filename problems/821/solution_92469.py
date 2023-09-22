def fatorial(num):
    """Função que recebe um número e retorna o fatorial.
    int -> int"""
    c = cont = 1
    while cont < num:
        cont += 1
        c *= cont
    return c