def  bolos(farinha,ovos,leite):
    """Essa função calcula a quantidade de bolos que será 
    possível fazer, com a quantidade de ingredientes que
    você tem em casa
    'farinha' - Xícaras de Farinha de trigo
    'ovos' - Ovos
    'leite' - Colheres de Sopa de Leite"""
    import math
    f = (math.floor (farinha/2))
    o = (math.floor (ovos/3))
    l = (math.floor (leite/5))
    return min (f,o,l)