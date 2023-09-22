def colchao(medidas,H,L):
    
    A,B,C = medidas
    
    if (A<=L) and (B<=H):
        return True
    elif (B<=L) and (C<=H):
        return True
    elif (A<=L) and (C<=H):
        return True
    elif (A<=H) and (B<=L):
        return True
    elif (C<=L) and (B<=H):
        return True
    elif (C<=L) and (A<=H):
        return True
    else:
        return False