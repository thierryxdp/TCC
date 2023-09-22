def colchao(medidas,H,L):
    """lel"""
    
    lista=[H,L]
    lista.sort()
    
    if medidas[0]<=lista[0] and medidas[1]<=lista[1]:
        return True
    else:
        False