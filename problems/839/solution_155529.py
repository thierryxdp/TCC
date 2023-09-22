def carros(n,c=5):
    """Retorna o número de carros necessários para levar uma
    quantidade n de pessoas para uma viagem. Esses carros
    possuem uma capacidade c
    :param n: int
    :param c: int
    :return: int
    round(c+0.5)"""
    return n//c