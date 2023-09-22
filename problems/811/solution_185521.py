def colchaoparececerto(medidas,H,L):
    """Funcao que diz se o colchao passa ou nao pela porta;
tuple,float,float -> bool"""
     
    A,B,C = medidas

    if max(A,B,C) > min(H,L) and min(B,C) > max(H,L):
        return False
    elif max(A,B,C) >= min(H,L) and min(B,C) <= max(H,L):
        return True