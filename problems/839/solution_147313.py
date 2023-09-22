def carros(p,c=5):
    """funcao que determina a quantidade de carros necessários para fazer uma viagem com p pessoas"""
    x = p/c
    math.ceil(x)
    return x