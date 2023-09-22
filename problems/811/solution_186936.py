def colchao(medidas,H,L):
    
    M = max(medidas)
    A = min(medidas)
    I = medidas - M - A
    
    if ((M < H) or (I[0] < H) or (I[0] < L)) and (A<L):
        return True
    else:
        return False