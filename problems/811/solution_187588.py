def colchao(medidas,H,L):
    
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if (A*B<=H*L) or (A*C<=H*L) or (C*B<=H*L):
        return True
    else:
        return False