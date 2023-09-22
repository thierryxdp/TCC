def colchao(medidas,H,L):
    """Funcao que diz se o colchao passa ou nao pela porta; tuple,float,float -> bool"""
    
    A,B,C = medidas
    passa = B <= H and B > L and C > H and C > L
    passa = B > H and B < L and C > H and C < L
    passa = B < H and B < L and C > H and C < L
    n_passa = B > H and B > L and C > H and C > L
    
    if passa:
        return True
    elif n_passa:
        return False