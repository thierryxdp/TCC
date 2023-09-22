bolos(A, B, C):
    """Função que calcula quantos bolos podem ser feitos,
    apenas com medidas exatas"""
    
    from math import *
    ingredientes = (A=2, B=3, C=5)
    bolo = gcd(A,B,C) == ingredientes
    
    return bolo