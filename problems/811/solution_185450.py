def colchao1(medidas,H,L):
    """Funcao que diz se o colchao passa ou nao pela porta; tuple,float,float -> bool"""
    
    A,B,C = medidas
    
    if B <= H and B > L and C > H and C > L:
        return True
    else:
        return False