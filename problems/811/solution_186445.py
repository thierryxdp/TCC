def colchao(medidas,H,L):
    
    porta = H * L
    
    
    if medidas == porta or medidas < porta:
        return True
    else:
        return False