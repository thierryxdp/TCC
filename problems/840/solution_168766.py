bolos(A, B=3, C=5):
    """Função que calcula quantos bolos podem ser feitos,
    apenas com medidas exatas"""
    
    from math import *
    ingredientes = ceil(A,B,C)
    
    return ingredientes