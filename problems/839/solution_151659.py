def carros(p,c=5):
    """calucla o numeros de carros necessarios para transportar p pessoas em carros com c capacidade
    int,int->float"""
    import math
    return math.ceil(p/c)