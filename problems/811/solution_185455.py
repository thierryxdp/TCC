def colchao(medidas,H,L):
    """Funcao que diz se o colchao passa ou nao pela porta; tuple,float,float -> bool"""
    
    A,B,C = medidas
    
    if B <= H and B > L and C > H and C > L:
        return True
    elif B > H and B > L and C > H and C > L or B > H and B < L and C > H and C < L or B < H and B < L and C > H and C < L or B > H and B < L and C > H and C < L:
        return False