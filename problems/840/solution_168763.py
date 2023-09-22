bolos(A, B, C):
    """Função que calcula quantos bolos podem ser feitos,
    apenas com medidas exatas"""
    
    from math import *
    A=2
    B=3
    C=5
    ingredientes = gcd(A),gcd(B),gcd(C)