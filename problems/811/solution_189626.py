def colchao (medidas,H,L):
    Hc = medidas[1]
    Hl = medidas[2]
    
    if (Hc*Hl <= H*L ):
        return True
    else:
        return False