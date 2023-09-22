def colchao (medidas,H,L):
    
    [A,B,C] = medidas
    
    if B<=H or B<=L or C<=H or C<=L:
        return True
    else:
        return False