import math
def carros (p, v=5):
    """ Considere p como numero de passageiros e v caso inserido valor, 
    como o numero de lugares por veiculo."""
    """ Foi utilizado o modulo ceil, para arredondar o numero para cima e ninguem ficar sem lugar"""
    T = p/v
    T = math.ceil(T)
    return T