def fatorial(num):
    """Dado um número, retorna o fatorial deste número"""
    c = contador = 1
    while contador < num:
        contador += 1
        c *= contador
    return c