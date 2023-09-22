def colchao_medidas(A,B,C,H,L):
    """retorna a expre~ssao booleana True ou False em razão do comparativo das medidad da porta e do colcão"""
    if A<L:
        return True
    if B<H:
        return True
    elif A>L:
        return False
    elif B>H:
        return False
    else: B==H:
        return True