def colchao(medidas,H,L):
    
    M = max(medidas)
    A = min(medidas)
    I = medidas[1]
    
    if ((M <= H) or (I <= H) or (I < L)) and (A < L):
        return True
    else:
        return False