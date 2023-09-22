import math
def num_bombons(dinheiro,preço):
    """calcula quantos bombons Pedrinho consegue comprar
    dados o dinheiro e opreço do bombom;int/float, int/float->int"""
    return min math.floor(dinheiro/preço)