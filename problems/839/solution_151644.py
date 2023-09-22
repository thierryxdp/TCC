def carros(p,a=5):
    """Recebe o número de pessoas (p) que irão e calcula o número de carros (c) necessários para transportá-los"""
    import math
    c = p/a
    c = math.ceil(c)
    return c