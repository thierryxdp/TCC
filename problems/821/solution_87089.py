def fatorial(numero):
    """função na qualdado um numero, calcula e
    retorna o fatorial deste numero"""
    f = 1
    while numero > 0:
        f *= numero
        numero -= 1
    return f