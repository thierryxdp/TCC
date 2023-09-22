def bolos(A,B,C):
    """calcula o número máximo de bolos possíveis de serem feitos
    com um número A de xícaras de farinha de trigo, B de ovos e C 
    de colheres de sopa de leite"""
    import math
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))