def carros(P,C=5):
    """função que calcula e retorna o nº exato de carros,dado nº de pessoas P e capacidade C. Quando C não informado, C será igual a 5
int,int> int"""
    import math
    return math.ceil(P//C)