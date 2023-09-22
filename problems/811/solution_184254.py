def colchao (medidas,H,L):
    
    [A,B,C] = medidas
    
    if medidas[1]<H or medidas[1]<L or medidas[2]<H or medidas[2]<L:
        return True
    else:
        return False