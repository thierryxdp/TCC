import math
def bolos(A,B,C):
    """função que ajuda o joao a saber a qtd de receitas que ele consegue fazer com os materiais que ele tem"""
    n1= math.ceil((A//2)-0.5)
    n2= math.ceil((B//3)-0.5)
    n3= math.ceil((C//5)-0.5)
    if n1==n2==n3:
    return n1