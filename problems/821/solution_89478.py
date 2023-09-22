def fatorial(x):
    """Função que dado um número x calcula o fatorial deste número"""
    num = 1
    while x >= 1:
        num = num * x
        x = x - 1
    return num