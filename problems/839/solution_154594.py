def carros(p,c=5):
    """divide o número de pessoas pela capacidade do carro e arredonda pra cima o resultado, retornando o número de carros necessário
    int,int->int"""
    import math
    return math.ceil(p/c)