def colchao(medidas,H,L):
    
    A,B,C = medidas
    medidas = A*B*C
    
    
    if H*L < A*B*C:
        return True 
    else:
        return False